import utils


def plant_pumpkins(path):
	growing_pumpkins = list(path)
	
	while len(growing_pumpkins) > 0:
		pumpkins_to_check = list(growing_pumpkins)
		for pos in growing_pumpkins:
			utils.go_to(pos)
			
			while get_entity_type() == Entities.Pumpkin and not can_harvest():
				pass
				
			if get_entity_type() == Entities.Pumpkin and can_harvest():
				pumpkins_to_check.remove(pos)
				continue
			
			utils.harvest_when_ready()
			utils.smart_plant(Entities.Pumpkin)
			utils.water()
		growing_pumpkins = list(pumpkins_to_check)


def farm(field):
	path = field["path"]
	
	utils.go_to(field["start"])
	plant_pumpkins(path)
	
	if field["type"] == "square":
		utils.go_to(field["start"])
		utils.harvest_when_ready()
		return
	
	for pos in path:
		utils.go_to(pos)
		utils.harvest_when_ready()
		return
	
	
def multi_drone():
	def check_and_plant(field):
		first_round = True
		
		while len(field) > 0:
			new_field = set()
			
			for pos in field:
				utils.go_to(pos)
				
				if not can_harvest() or first_round:
					utils.smart_plant(Entities.Pumpkin)
					utils.water()
					new_field.add(pos)
					
			field = set(new_field)
			first_round = False
		
		
	def worker():
		x = get_pos_x()
		field = set()
		for y in range(0, get_world_size()):
			field.add((x, y))
			
		check_and_plant(field)
		
		return
	

	drones = []
	
	for x in range(0, get_world_size()):
		utils.go_to(x, 0)
		
		if num_drones() < max_drones():
			drones.append(spawn_drone(worker))
	
	worker()
	
	for drone in drones:
		wait_for(drone)
		
	harvest()