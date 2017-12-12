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

def main():
	with open('in.txt') as f:
		txt = f.read()

	directions = txt.split(',')

	c = Counter(directions)
	print c

	c = cancel(c,'n','s')
	c = cancel(c,'ne','sw')
	c = cancel(c,'nw','se')

	c = collapse(c,'ne','nw','n')
	c = collapse(c,'se','sw','s')

	print c

if __name__ == '__main__':
	main()