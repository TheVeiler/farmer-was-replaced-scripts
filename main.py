import utils

import Game
import Field

drone_id = Game.register_drone()

start_pos = (0, 0)
side = 8
is_empty = False
ressources = [Items.Power]
clear_field_beforehand = True
	
Game.set_field(drone_id, Field.square(start_pos, side, is_empty), {"no_check": not clear_field_beforehand})
Game.farm(drone_id, ressources)