import utils


def harvest_and_plant():
	utils.harvest_when_ready()
	utils.smart_plant(Entities.Grass)
	#utils.water()
		
		
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
		while True:
			move(North)
			harvest()
			
	world_size = get_world_size()
	n = world_size - 1
	clear()
	spawn_drones()
	utils.wait_ticks(200)
	worker()