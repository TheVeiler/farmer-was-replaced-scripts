import utils


def turn_left():
	global facing
	facing = left_from[facing]

def turn_right():
	global facing
	facing = right_from[facing]

def move_forward():
	global facing
	move(facing)

def v0():
	while True:
		size = get_world_size()
		facing = North
	
		clear()
		utils.go_to(0, 0)
		utils.smart_plant(Entities.Bush)
		use_item(Items.Weird_Substance, size * 2 ** (num_unlocked(Unlocks.Mazes) - 1))
	
		treasure_pos = measure()
	
		left_from = {North: West, East: North, South: East, West: South}
		right_from = {North: East, East: South, South: West, West: North}
	
		while utils.get_pos() != treasure_pos:
			if can_move(left_from[facing]):
				turn_left()
				move_forward()
			else :
				while not can_move(facing):
					turn_right()
				move_forward()
	
		harvest()
		
def multi_drone():
	clear()
	utils.go_to(0, 0)
	utils.smart_plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1))

	facing = None
	coming_from = None
	forward_from = {North: South, East: West, South: North, West: East}
	
	def explore():
		global facing
		global coming_from
		global forward_from
		
		if facing != None:
			move(facing)
		
		# check if maze is finished
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True
		if get_entity_type() != Entities.Hedge:
			return
			
		possible_directions = []
		for dir in [North, East, South, West]:
			if can_move(dir) and coming_from != dir:
				possible_directions.append(dir)
				
		if len(possible_directions) == 0:
			return # dead-end
			
		while len(possible_directions) - 1 > max_drones() - num_drones():
			# that is highly problematic
			# if the total number of possible paths exceeds max_drones(), all the drones will be stuck in place forever
			pass
				
		for dir in possible_directions:
			facing = dir
			coming_from = forward_from[dir]
			if dir != possible_directions[len(possible_directions) - 1]:
				spawn_drone(explore)
			
		explore()
	
	explore()
	

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
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, slime_quantity)
			harvest()
	
	world_size = get_world_size()
	id_drone = 0
	slime_quantity = 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	clear()
	
	spawn_drones(farm_worker)
	utils.wait_ticks(200)
	farm_worker()