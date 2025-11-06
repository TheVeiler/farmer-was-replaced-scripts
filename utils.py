def do_everywhere(fct = do_a_flip):
	reset_pos()
	for x in range(get_world_size()):
		for i in range(get_world_size()):
			if i > 0:
				if get_pos_x() % 2 == 0:
					move(North)
				else:
					move(South)
				wait_ticks(200)
			fct()
		move(East)


def get_pos():
	return get_pos_x(), get_pos_y()


def go_to(x = (0, 0), y = None): # O(27+n) ticks
	if y == None: # 2 ticks
		x, y = x

	world_size = get_world_size() # 1 tick
		
	posX = get_pos_x() # 1 tick
	distX = abs(x - posX) # 2 ticks
	distX = min(distX, world_size - distX) # 2 ticks
	if (posX + distX) % world_size == x: # 4 ticks
		dirX = East
	else:
		dirX = West
		
	posY = get_pos_y() # 1 tick
	distY = abs(y - posY) # 2 ticks
	distY = min(distY, world_size - distY) # 2 ticks
	if (posY + distY) % world_size == y: # 4 ticks
		dirY = North
	else:
		dirY = South
	
	for _ in range(distX):
		move(dirX)
	for _ in range(distY):
		move(dirY)
	
	
def harvest_when_ready(turbo_mode = False):
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
		return

	while not can_harvest():
		if turbo_mode and num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
		
	harvest()
	

def random_elem(list):
	return list[random() * len(list)]
	
	
def reset_pos():
	go_to(0, 0)
		
		
def reset_all():
	clear()
	wait_ticks(200)


def smart_plant(entity):
	needs_tilling = {Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus}
	if entity in needs_tilling: 
		if get_ground_type() != Grounds.Soil:
			till()
	plant(entity)
	
	
def till_farm():
	def till_column():
		for y in range(get_world_size()):
			go_to(x,y)
			till()
		return
		
	for x in range(get_world_size()):
		go_to(x,0)
		if x < get_world_size() - 1:
			spawn_drone(till_column)
	till_column()
	return


def wait_ticks(ticks):
	for _ in range(ticks - 3): # 3 ticks
		pass
		
		
def wait_seconds(seconds):
	if seconds <= 0:
		return
	for i in range(seconds):
		do_a_flip()


def water():
	while not can_harvest() and get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)