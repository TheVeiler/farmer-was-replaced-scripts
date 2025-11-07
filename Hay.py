import utils


def harvest_and_plant():
	utils.harvest_when_ready()
	utils.smart_plant(Entities.Grass)
	#utils.water()
	
def farm(field):
	for pos in field["path"]:
		utils.go_to(pos)
		harvest_and_plant()
		

def synced_multi_drone():
	def set_position():
		for _ in range(id_drone):
			pass # cancels out tick from id_drone -= 1
			move(East)
			
	def spawn_drones(worker):
		global id_drone
		id_drone = world_size - 1
		for _ in range(world_size - 1):
			spawn_drone(worker)
			id_drone -= 1 # 1 tick
	
	def farm_worker():
		set_position()
		while True:
			harvest()
			move(North)
			
	world_size = get_world_size()
	id_drone = 0
	clear()
	
	spawn_drones(farm_worker)
	utils.wait_ticks(200)
	farm_worker()