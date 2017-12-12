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

	# Start traversing edges and building connected sets.

	subgraphs = [set([x]) for x in range(1,2000)]

	for s,d in edges:
		

		for g1 in subgraphs:
			for g2 in subgraphs:
				if not g1 == g2 and s in g1 and d in g2:
						print g1, g2
						subgraphs_new = subgraphs

						subgraphs_new.append(g1.union(g2))
						subgraphs_new.remove(g1)
						subgraphs_new.remove(g2)

	print subgraphs

if __name__ == '__main__':
	main()