s = 6
S = 36
set_world_size(s)

dirs = [North,
North, North, North, North, East,
South, South, South, South, East,
North, North, North, North, East,
South, South, South, South, East,
North, North, North, North, East,
South, South, South, South, South,
West, West, West, West, West]

for i in range(S):
	if i % 2:
		plant(Entities.Bush)
	else:
		plant(Entities.Tree)
		use_item(Items.Water)
	move(dirs[i])
	
i = 0

while num_items(Items.Wood) < 500000000:
	harvest()
	if i % 2:
		plant(Entities.Bush)
	else:
		plant(Entities.Tree)
		use_item(Items.Water)
	move(dirs[i])
	i = (i + 1) % S