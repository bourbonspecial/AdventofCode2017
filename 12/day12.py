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

def merge_graphs(graphs,edges):
	"""
	Take a list of graphs and edges and do one pass of consolidation.
	"""

	new_graphs = []

	for s,d in edges:
		for g1 in graphs:
			for g2 in graphs:
				if not g1 == g2 and s in g1 and d in g2:
					new_graphs.append(g1.union(g2))

	for g in graphs:
		for ng in new_graphs:
			if g.intersect(ng):
				break
		else:
			new_graphs.append(g)

	return new_graphs

def main():
	edges = parse()
	graphs = [set([x]) for x in range(2000)]
	
	for _ in range(1):
		graphs = merge_graphs(graphs,edges)

	print graphs

if __name__ == '__main__':
	main()