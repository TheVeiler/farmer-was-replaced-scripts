def wait_ticks(ticks):
	for _ in range(ticks - 3): # 3 ticks
		pass

def spawn_drones(worker):
	global id_drone
	id_drone = world_size - 1
	for _ in range(world_size - 1):
		drones.append(spawn_drone(worker))
		id_drone -= 1 # 1 tick
		
def set_position():
	for _ in range(id_drone):
		pass # cancels out tick from id_drone -= 1
		move(East)
	
def setup_worker():
	set_position()
	till()
	plant(Entities.Sunflower)
	while measure() > 7:
		harvest()
		plant(Entities.Sunflower)
	
def farm_worker():
	set_position()
	till()
	use_item(Items.Water, 3)
	while num_items(Items.Power) < 100000:
		plant(Entities.Sunflower)
		petals = measure()
		use_item(Items.Water)
		wait_ticks(9000)
		for i in range(15, 6, -1):
			if i == petals:
				harvest()
			else:
				wait_ticks(200)

world_size = get_world_size()
id_drone = 0
clear()

drones = []
spawn_drones(setup_worker)
wait_ticks(200)
setup_worker()

move(North)
for drone in drones:
	wait_for(drone)

spawn_drones(farm_worker)
wait_ticks(200)
farm_worker()
