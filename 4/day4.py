# https://adventofcode.com/2017/day/4

__author__ = 'Remus Knowles <remknowles@gmail.com>'

from math import factorial

def load():
	"""
	Read in word list.
	"""
	cnt = 0
	with open(r"in.txt", 'r') as f:
		for r in f:
			if len(r.split()) == len(set(r.split())):
				cnt += 1

	return cnt

def main():
	print load()

if __name__ == '__main__':
	main()