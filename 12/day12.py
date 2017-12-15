# https://adventofcode.com/2017/day/12

__author__ = 'Remus Knowles <remknowles@gmail.com>'

from datetime import datetime

def parse():
	"""
	Take the input and turn it in to a list of edges.
	"""

	edges = []

	with open('in.txt') as f:
		for r in f:
			src = int(r.split(' <-> ')[0])
			dests = [int(x) for x in r.split(' <-> ')[1].split(',')]
			edges += [(src,dest) for dest in dests]

	return edges

def main():
	start = datetime.now()
	edges = parse()

	groups_upper_bound = 2000
	group_construct_iters = 30
	g = set([0])

	groups = []

	for i in range(groups_upper_bound):
		g = set([i])
		for _ in xrange(group_construct_iters):
			for s, d in edges:
				if s in g or d in g:
					g.add(s)
					g.add(d)
		groups.append(g)

	clean_groups = []
	for g in groups:
		if not g in clean_groups:
			clean_groups.append(g)

	print datetime.now() - start
	print len(clean_groups)

if __name__ == '__main__':
	main()