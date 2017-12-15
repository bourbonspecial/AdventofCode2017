# https://adventofcode.com/2017/day/12

__author__ = 'Remus Knowles <remknowles@gmail.com>'

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
	edges = parse()
	g = set([0])

	for _ in xrange(10):
		for s, d in edges:
			if s in g or d in g:
				g.add(s)
				g.add(d)

	print len(g)

if __name__ == '__main__':
	main()