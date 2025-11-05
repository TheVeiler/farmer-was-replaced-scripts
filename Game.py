import utils

import Hay
import Wood
import Carrots
import Pumpkins
import Cacti
import Sunflowers
import Bones


drones = []
fields = {}

scripts = {}
scripts[Items.Hay] = Hay
scripts[Items.Wood] = Wood
scripts[Items.Carrot] = Carrots
scripts[Items.Pumpkin] = Pumpkins
scripts[Items.Cactus] = Cacti
scripts[Items.Power] = Sunflowers
scripts[Items.Bone] = Bones


def register_drone():
	change_hat(Hats.Straw_Hat)
	drone_id = len(drones)
	drones.append(drone_id)
	return drone_id
	

def set_field(drone_id, field, options = {}):
	fields[drone_id] = field
	
	if "no_check" not in options:
		options["no_check"] = False
	
	if not options["no_check"]:
		for pos in field["path"]:
			utils.go_to(pos)
			utils.harvest_when_ready()
	
	utils.go_to(field["start"])
	do_a_flip()

	return fields[drone_id]
	
	
def farm(drone_id, items):
	while True:
		farm_once(drone_id, items)


def farm_once(drone_id, items):
	for item in items:
		scripts[item].farm(fields[drone_id])