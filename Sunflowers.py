import utils

petals = {}
nbr_planted = 0


def init_list():
	for n in range(7, 16):
		petals[n] = []
		
		
def plant_sunflower():
	global nbr_planted
	
	utils.smart_plant(Entities.Sunflower)
	utils.water()
	
	if get_entity_type() == Entities.Sunflower:
		nbr_planted += 1
		petals[measure()].append(utils.get_pos())


def farm(field):
	global nbr_planted
	
	path = field["path"]
	
	if len(path) < 10:
		print("Must have at least 10 sunflowers.")
		return
	
	nbr_planted = 0
	n = 15
	init_list()
	
	for pos in path:
		utils.go_to(pos)
		plant_sunflower()
		
	while nbr_planted >= 10:
		while len(petals[n]) == 0 and n > 6:
			n -= 1
			
		if n == 6:
			print("No more sunflowers.")
			return
	
		utils.go_to(petals[n][0])
		utils.harvest_when_ready()
		petals[n].pop(0)
		nbr_planted -= 1
		
		
def synced_multi_drone():
	def spawn_drones():
		global n
		for _ in range(world_size - 1):
			spawn_drone(worker)
			n -= 1 # 1 tick
			
	def worker():
		for _ in range(n):
			pass # cancels out tick from n -= 1
			move(East)
		# ---
		for _ in range(world_size):
			till()
			use_item(Items.Water, 4)
			move(North)
		while True:
			for _ in range(world_size):
				plant(Entities.Sunflower)
				use_item(Items.Water)
				move(North)
			for petals in range(15, 6, -1):
				for _ in range(world_size):
					if measure() == petals:
						harvest()
					else:
						utils.wait_ticks(200)
					move(North)
			
	world_size = get_world_size()
	n = world_size - 1
	
	clear()
	spawn_drones()
	utils.wait_ticks(200)
	worker()