def worker():
	for _ in range(n):
		move(East)
	while num_items(Items.Hay) < 2000000000: # 3 ticks
		move(North)
		harvest()

n = 31
loop = range(get_world_size() - 1) # 3 ticks
for _ in loop: # 1 tick
	spawn_drone(worker) # 200 ticks
	n -= 1 # 1 tick
for _ in range(197): # 2 ticks
	pass # 1 tick
worker()