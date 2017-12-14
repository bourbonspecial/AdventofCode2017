# https://adventofcode.com/2017/day/10 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

inp = [206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3]

def main():
	start = range(256)
	skip = 0
	pt = 0

	for el in inp:
		# Rotate list
		rstart = [start[(i+pt) % len(start)] for i in range(len(start))]

		new_start = rstart[:el][::-1] + rstart[el:]

		# Rotate the list back again
		start = [new_start[(i-pt) % len(new_start)] for i in range(len(new_start))]

		pt += el + skip
		skip += 1

	print start[0] * start[1]

if __name__ == '__main__':
	main()