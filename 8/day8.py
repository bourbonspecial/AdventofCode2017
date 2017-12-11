# https://adventofcode.com/2017/day/8

__author__ = 'Remus Knowles <remknowles@gmail.com>'

import pprint

def main():
	registers = {}
	large = 0

	with open('in.txt') as f:
		for r in f:
			target_reg = r.split()[0]
			cond_reg = r.split(' if ')[1].split()[0]

			if not target_reg in registers:
				registers[target_reg] = 0

			if not cond_reg in registers:
				registers[cond_reg] = 0

			cond = 'registers["' + cond_reg + '"]' + ''.join(r.split(' if ')[1].split()[1:])
			quant = int(r.split()[2])

			if eval(cond):
				if 'inc' in r:
					registers[target_reg] += quant
				elif 'dec' in r:
					registers[target_reg] -= quant
				else:
					print 'not inc or dec :('

				if registers[target_reg] >= large:
					large = registers[target_reg]

	pprint.pprint(large)

if __name__ == '__main__':
	main()