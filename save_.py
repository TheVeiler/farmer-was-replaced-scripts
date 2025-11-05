import utils


def setup_farm():
	def till_column():
		for y in range(get_world_size()):
			utils.go_to(x,y)
			till()
		return
		
	for x in range(get_world_size()):
		utils.go_to(x,0)
		if x < get_world_size() - 1:
			spawn_drone(till_column)
	till_column()
	return
	

def harvest_worker():
	change_hat(Hats.Green_Hat)
	utils.go_to(prev_pos)
	wait_for(harvest_drone)
	utils.harvest_when_ready()
	return
	
	
def find_empty_slot():
	while get_entity_type() != None:
		move(East)
	return
	
	
def plant_worker():
	global prev_pos
	global seed
	global next_pos
	global harvest_drone
	
	change_hat(Hats.Gray_Hat)
	while True:
		prev_pos = utils.get_pos()
		seed, next_pos = get_companion()
		utils.go_to(next_pos)
		while num_drones() == max_drones():
			pass
		harvest_drone = spawn_drone(harvest_worker)
		find_empty_slot()
		utils.smart_plant(seed)
		utils.water()
	
	
def null():
	return
	

utils.reset_all()
set_world_size(16)
setup_farm()
utils.go_to(0,0)
seed, next_pos = Entities.Grass, utils.get_pos()
utils.smart_plant(seed)
harvest_drone = spawn_drone(null)
plant_worker()