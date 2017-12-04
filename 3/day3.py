# https://adventofcode.com/2017/day/3

__author__ = 'Remus Knowles <remknowles@gmail.com>'

def which_layer(integer):
	"""
	Work out which layer an integer is in.
	"""

	c = 1
	while ((2*c - 1)*(2*c - 1)) <= integer:
		c += 1

	return c

def layer_rows(layer):
	"""
	Given a layer return each row as a list.
	"""

	els = range((2*(layer-1)-1)*(2*(layer-1)-1) + 1, (2*layer-1)*(2*layer-1) + 1)

	side_length = len(els) / 4

	return [els[:side_length], els[side_length:2*side_length], els[2*side_length:3*side_length], els[3*side_length:]]

def dist(integer):
	"""
	Return the distance from center.
	"""

	if integer == 1:
		return 0

	c = which_layer(integer)
	rows = layer_rows(c)
	l = len(rows[0])

	mid = (l / 2) - 1

	for r in rows:
		if integer in r:
			list_pos = r.index(integer)

	return c + abs(mid - list_pos) - 1

def main():
	print dist(1024)

if __name__ == '__main__':
	main()