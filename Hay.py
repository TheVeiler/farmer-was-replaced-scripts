#import utils


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
		
		loop = range(get_world_size() - 1) # 3 ticks
		for _ in loop: # 1 tick
			spawn_drone(worker) # 200 ticks
			n -= 1 # 1 tick
	
	def worker():
		for _ in range(n):
			move(East)
		while True:
			move(North)
			harvest()
	
	n = 31
	clear() # 200 ticks
	spawn_drones() # 6235 ticks
	for _ in range(197): # 2 ticks
		pass
	worker()