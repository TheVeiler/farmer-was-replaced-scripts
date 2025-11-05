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
	def spawn_drones():
		global n
		loop = range(world_size - 1)
		for _ in loop:
			spawn_drone(worker)
			n -= 1 # 1 tick
	
	def worker():
		for _ in range(n):
			pass # cancels out tick from n -= 1
			move(East)
		mod = get_pos_x() % 2
		loop = 0
		while True:
			harvest()
			if mod == get_pos_y() % 2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			if loop < world_size:
				use_item(Items.Water)
			move(North)
			loop = (loop + 1) % (8 * world_size)
			
	world_size = get_world_size()
	n = world_size - 1
	clear()
	spawn_drones()
	utils.wait_ticks(200)
	worker()