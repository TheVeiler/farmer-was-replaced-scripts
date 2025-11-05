import utils


def harvest_and_plant():
	utils.harvest_when_ready()
	utils.smart_plant(Entities.Tree)
	utils.water()
		
		
def farm(field):
	for pos in field["path"]:
		utils.go_to(pos)
		harvest_and_plant()
		
		
def multi_drone():
	def worker():
		x = get_pos_x()
		field = set()
		for y in range(get_world_size()):
			field.add((x, y))
			
		for pos in field:
			utils.go_to(pos)
			if get_pos_x() % 2 == get_pos_y() % 2:
				utils.smart_plant(Entities.Tree)
				utils.water()
			else:
				utils.smart_plant(Entities.Bush)
				#utils.water()
			
			
		for pos in field:
			utils.go_to(pos)
			utils.harvest_when_ready()
		
		return
	

	drones = []
	
	for x in range(get_world_size()):
		utils.go_to(x, 0)
		
		if num_drones() < max_drones():
			drones.append(spawn_drone(worker))
	
	worker()
	
	for drone in drones:
		wait_for(drone)