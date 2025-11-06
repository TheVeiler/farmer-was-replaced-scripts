import utils


def harvest_and_plant():
	utils.harvest_when_ready()
	utils.smart_plant(Entities.Tree)
	utils.water()
		
		
def farm(field):
	for pos in field["path"]:
		utils.go_to(pos)
		harvest_and_plant()
		
		
def synced_multi_drone():
	def spawn_drones():
		global n
		for _ in range(world_size - 1):
			spawn_drone(worker)
			n -= 1 # 1 tick
			
	def smart_water():
		global water_loop
		if water_loop < world_size:
			use_item(Items.Water)
		water_loop = (water_loop + 1) % (water_reset_loop * world_size)
	
	def worker():
		for _ in range(n):
			pass # cancels out tick from n -= 1
			move(East)
		# ---
		for _ in range(world_size):
			use_item(Items.Water, 4)
			move(North)
		mod = get_pos_x() % 2
		while True:
			harvest()
			if mod == get_pos_y() % 2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			smart_water()
			move(North)
			
	world_size = get_world_size()
	n = world_size - 1
	water_loop = 0
	water_reset_loop = 14
	
	clear()
	spawn_drones()
	utils.wait_ticks(200)
	worker()