# https://adventofcode.com/2017/day/7 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

class Tower(object):
	def __init__(self,name,weight,supports):
		self.name = name
		self.weight = weight
		self.supports = supports
		# self.supports = [t for t in all_towers if t.name in supports]

def weigh(tower,all_towers):
	"""
	Find the total weight of a tower.
	"""

	if not tower.supports:
		return tower.weight

	return sum([weigh(t,all_towers) for t in all_towers if t.name in tower.supports]) + tower.weight

def main():
	with open('in.txt') as f:
		rows = f.read().split('\n')

	all_towers = []

	for r in rows:
		name = r.split()[0]
		weight = int(r.split()[1].replace('(','').replace(')',''))
		if len(r.split('->')) > 1:
			supports = r.split(' -> ')[-1].split(', ')
		else:
			supports = []

		all_towers.append(Tower(name, weight, supports))

	print 'Seconds'
	seconds_names = ['twimhx', 'wfdiqkg', 'guuri', 'qwada', 'mwsivlf']
	seconds = [t for t in all_towers if t.name in seconds_names]

	for t in seconds:
		w = weigh(t,all_towers)
		print t.name, w

	print 'thirds'
	thirds_names = ['wfkcsb', 'qlboef', 'pkowhq']
	thirds = [t for t in all_towers if t.name in thirds_names]

	for t in thirds:
		w = weigh(t,all_towers)
		print t.name, w

	print 'fourths'
	thirds_names = ['zfrsmm', 'tlskukk', 'fqkbscn', 'mlafk']
	thirds = [t for t in all_towers if t.name in thirds_names]

	for t in thirds:
		w = weigh(t,all_towers)
		print t.name, w

	print 'fifths'
	thirds_names = ['ixoiuh', 'jdxth']
	thirds = [t for t in all_towers if t.name in thirds_names]

	for t in thirds:
		w = weigh(t,all_towers)
		print t.name, w

if __name__ == '__main__':
	main()