# https://adventofcode.com/2017/day/7 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

class Tower(object):
	def __init__(self,name,weight,supports):
		self.name = name
		self.weight = weight
		self.supports = supports
		# self.supports = [t for t in all_towers if t.name in supports]

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

	counter = {t.name:0 for t in all_towers}

	for t in all_towers:
		for s in t.supports:
			counter[s] += 1

	for n in counter:
		if counter[n] == 0:
			print n

if __name__ == '__main__':
	main()