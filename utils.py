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


def go_to(x = (0, 0), y = None):
	if y == None:
		x, y = x

	#posX = get_pos_x()
	#if (posX <= x and x - posX <= get_world_size() / 2) or (posX >= x and x - posX <= -get_world_size() / 2):
	#	dirX = East
	#	distX = min(abs(posX - x), abs(x + get_world_size() - posX))
	#else:
	#	dirX = West
	#	distX = min(abs(x - posX), abs(posX + get_world_size() - x))
	#	
	#posY = get_pos_y()
	#if (posY <= y and y - posY <= get_world_size() / 2) or (posY >= y and y - posY <= -get_world_size() / 2):
	#	dirY = North
	#	distY = min(abs(posY - y), abs(y + get_world_size() - posY))
	#else:
	#	dirY = South
	#	distY = min(abs(y - posY), abs(posY + get_world_size() - y))
		
	posX = get_pos_x()
	distX = min(abs(x - posX), get_world_size() - abs(x - posX))
	if (posX + distX) % get_world_size() == x:
		dirX = East
	else:
		dirX = West
		
	posY = get_pos_y()
	distY = min(abs(y - posY), get_world_size() - abs(y - posY))
	if (posY + distY) % get_world_size() == y:
		dirY = North
	else:
		dirY = South
	
	for i in range(distX):
		move(dirX)
	for i in range(distY):
		move(dirY)
		
	#wait_ticks(200 * (distX + distY))
	
	
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
	if ticks <= 0:
		return
	timestamp_before = get_tick_count()
	while get_tick_count() < timestamp_before + ticks:
		pass
		
		
def wait_seconds(seconds):
	if seconds <= 0:
		return
	for i in range(seconds):
		do_a_flip()


def water():
	while not can_harvest() and get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)