import utils


def square(start = (0, 0), side = 4, is_empty = False):
	field = rect(start, side, side, is_empty)
	field["type"] = "square"
	return field


def rect(start = (0, 0), height = 3, width = 2, is_empty = False):
	field = {"type": "rect", "start": start, "height": height, "width": width, "is_empty": is_empty, "path": []}

	startX, startY = start

	if startX < 0 or startX + width - 1 >= get_world_size() or startY < 0 or startY + height - 1 >= get_world_size():
		print("Coordinates must be in field.")
		return field
	if height < 2 or width < 2:
		print("Field must be at least 2x2.")
		return field
	
	if is_empty == True:
		for y in range(startY, startY + height - 1):
			field["path"].append((startX, y))
		for x in range(startX, startX + width - 1):
			field["path"].append((x, startY + height - 1))
		for y in range(startY + height - 1, startY, -1):
			field["path"].append((startX + width - 1, y))
		for x in range(startX + width - 1, startX, -1):
			field["path"].append((x, startY))
		return field
	
	if width % 2 == 1:
		print("Width must be even for a full rectangle.")
		return field
	
	field["path"].append(start)
	for x in range(startX, startX + width, 2):
		for y in range(startY + 1, startY + height):
			field["path"].append((x, y))
		for y in range(startY + height - 1, startY, -1):
			field["path"].append((x + 1, y))
	for x in range(startX + width - 1, startX, -1):
		field["path"].append((x, startY))
	return field