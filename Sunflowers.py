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
		
		
def multi_drone():
	def plant_worker():
		x = get_pos_x()
		for y in range(0, get_world_size()):
			utils.go_to(x, y)
			
			utils.smart_plant(Entities.Sunflower)
			utils.water()
		return
		
		
	def harvest_worker():
		x = get_pos_x()
		for y in range(0, get_world_size()):
			utils.go_to(x, y)
			
			if measure() == petals:
				utils.harvest_when_ready()
		return
	
	
	# plant_worker
	drones = []
	
	for x in range(0, get_world_size()):
		utils.go_to(x, 0)
		
		if num_drones() < max_drones():
			drones.append(spawn_drone(plant_worker))
			
	plant_worker()
	
	for drone in drones:
		wait_for(drone)
		
	
	# harvest_worker
	for petals in range(15, 6, -1):
		drones = []
		
		for x in range(0, get_world_size()):
			utils.go_to(x, 0)
			
			if num_drones() < max_drones():
				drones.append(spawn_drone(harvest_worker))
				
		harvest_worker()
		
		for drone in drones:
			wait_for(drone)
	
	
	# harvest
	utils.go_to(0, 0)
	harvest()