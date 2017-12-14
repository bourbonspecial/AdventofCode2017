# https://adventofcode.com/2017/day/10 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

from operator import xor

inp = 'oh hi there'

def knot_hash(inp, rounds=64):
	ls = range(256)
	inp = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
	skip = 0
	pt = 0

	for _ in range(rounds):
		for el in inp:
			# Rotate list
			rls = [ls[(i+pt) % len(ls)] for i in range(len(ls))]

			new_ls = rls[:el][::-1] + rls[el:]

			# Rotate the list back again
			ls = [new_ls[(i-pt) % len(new_ls)] for i in range(len(new_ls))]

			pt += el + skip
			skip += 1

	blocks = [ls[i * 16:(i + 1) * 16] for i in range(len(ls) / 16)]
	dense = []
	for b in blocks:
		s = b[0]
		for el in b[1:]:
			s = xor(s,el)
		dense.append(s)

	dense = ''.join([str(hex(i)).replace('0x','') for i in dense])

	return dense

def main():	
	print knot_hash('206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3')

if __name__ == '__main__':
	main()