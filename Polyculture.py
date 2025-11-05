import utils


def find_empty_slot():
	while get_entity_type() != None:
		move(East)
	return


def find_inactive_drone(drones_in_area):
	for i in range(max_drones_per_area - 1):
		if has_finished(drones_in_area[i]):
			return i
	return -1


def plant_worker():
	global seed
	global prev_pos
	global next_pos
	
	drones_in_area = []
	for i in range(max_drones_per_area - 1):
		drones_in_area.append(spawn_drone(null))
	
	def harvest_worker():
		change_hat(Hats.Green_Hat)
		utils.go_to(prev_pos)
		wait_for(drones_in_area[id_drone - 1])
		utils.harvest_when_ready()
		return

	change_hat(Hats.Gray_Hat)
	while True:
		prev_pos = utils.get_pos()
		seed, next_pos = get_companion()
		utils.go_to(next_pos)
		id_drone = -1
		while id_drone < 0:
			id_drone = find_inactive_drone(drones_in_area)
			pass
		drones_in_area[id_drone] = spawn_drone(harvest_worker)
		find_empty_slot()
		utils.smart_plant(seed)
		utils.water()
	return
	
	
def null():
	return
	

utils.reset_all()
utils.till_farm()
utils.go_to(0,0)

number_areas = 4
max_drones_per_area = max_drones() // number_areas

for area in range(number_areas):
	x = area * get_world_size() // number_areas
	y = area * get_world_size() // number_areas
	utils.go_to(x,y)
	
	seed = Entities.Grass
	prev_pos = None
	next_pos = utils.get_pos()
	
	utils.smart_plant(seed)
	
	if area < number_areas - 1:
		spawn_drone(plant_worker)
	
plant_worker()