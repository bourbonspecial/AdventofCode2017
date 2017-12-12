# https://adventofcode.com/2017/day/11

__author__ = 'Remus Knowles <remknowles@gmail.com>'

from collections import Counter

def cancel(d,k1,k2):
	"""
	For keys that cancel each other out'
	"""

	if d[k1] > d[k2]:
		d[k1] = d[k1] - d[k2]
		d[k2] = 0
	else:
		d[k2] = d[k2] - d[k1]
		d[k1] = 0

	return d

def collapse(d,k1,k2,k3):
	"""
	For keys k1, k2 that cancel down to k3.
	"""

	if d[k1] > d[k2]:
		d[k3] += d[k2]
		d[k1] = d[k1] - d[k2]
		d[k2] = 0
	else:
		d[k3] += d[k1]
		d[k2] = d[k2] - d[k1]
		d[k1] = 0

	return d

def dist(directions):
	"""
	Calculate dist from array of directions.
	"""

	c = Counter(directions)

	c = cancel(c,'n','s')
	c = cancel(c,'ne','sw')
	c = cancel(c,'nw','se')

	c = collapse(c,'ne','nw','n')
	c = collapse(c,'se','sw','s')

	return sum(c.values())

def main():
	with open('in.txt') as f:
		txt = f.read()

	directions = txt.split(',')

	print max([dist(directions[:i]) for i in range(1,len(directions) + 1)])

if __name__ == '__main__':
	main()