import utils


def farm(field):
	path = field["path"]
	
	utils.go_to(field["start"])
	change_hat(Hats.Dinosaur_Hat)
	
	ticks = 400
	eaten = 0
	
	while eaten < len(path) - 2:
		for pos in path:
			if get_entity_type() == Entities.Apple:
				eaten += 1
				ticks -= ticks * 0.03 // 1
			utils.go_to(pos)
			utils.wait_ticks(ticks - 200) # go_to() spent 200 already

	change_hat(Hats.Straw_Hat)