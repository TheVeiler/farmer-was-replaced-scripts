import utils


def sort_column(x, startY, endY):
	for y in range(startY, endY + 1):
		utils.go_to(x, y)
		
		deltaY = 0
		while y > startY and measure() < measure(South):
			swap(South)
			deltaY += 1
			y -= 1
			utils.go_to(x, y)
		y += deltaY


def sort_row(y, startX, endX):
	for x in range(endX, startX - 1, -1):
		utils.go_to(x, y)
		
		deltaX = 0
		while x < endX and measure() > measure(East):
			swap(East)
			deltaX -= 1
			x += 1
			utils.go_to(x, y)
		x -= deltaX


def farm(field):
	path = field["path"]
	startX, startY = field["start"]
	height = field["height"]
	width = field["width"]

	for pos in path:
		utils.go_to(pos)
		utils.smart_plant(Entities.Cactus)

	for x in range(startX, startX + width):
		sort_column(x, startY, startY + height - 1)
			
	for y in range(startY + height - 1, startY - 1, -1):
		sort_row(y, startX, startX + width - 1)
			
	utils.go_to(field["start"])
	utils.harvest_when_ready()
	
	
def multi_drone():
	def plant_worker():
		x = get_pos_x()
		for y in range(0, get_world_size()):
			utils.go_to(x, y)
			
			utils.smart_plant(Entities.Cactus)
			#utils.water()
		return
		
		
	def sort_col_worker():
		x = get_pos_x()
		for y in range(0, get_world_size()):
			utils.go_to(x, y)
			
			deltaY = 0
			while y > 0 and measure() < measure(South):
				swap(South)
				deltaY += 1
				y -= 1
				utils.go_to(x, y)
			y += deltaY
		return
		
		
	def sort_row_worker():
		y = get_pos_y()
		for x in range(0, get_world_size()):
			utils.go_to(x, y)
			
			deltaX = 0
			while x > 0 and measure() < measure(West):
				swap(West)
				deltaX += 1
				x -= 1
				utils.go_to(x, y)
			x += deltaX
		return
	
	
	# workers that spawn on first row
	workers = {plant_worker, sort_col_worker}
	for worker in workers:
		drones = []
		
		for x in range(0, get_world_size()):
			utils.go_to(x, 0)
			
			if num_drones() < max_drones():
				drones.append(spawn_drone(worker))
				
		worker()
		
		for drone in drones:
			wait_for(drone)
	
	# workers that spawn on first col
	workers = {sort_row_worker}
	for worker in workers:
		drones = []
		
		for y in range(0, get_world_size()):
			utils.go_to(0, y)
			
			if num_drones() < max_drones():
				drones.append(spawn_drone(worker))
				
		worker()
		
		for drone in drones:
			wait_for(drone)
	
	# harvest
	utils.go_to(0, 0)
	harvest()