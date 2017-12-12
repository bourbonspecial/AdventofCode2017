# https://adventofcode.com/2017/day/10 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

inp = [206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3]
inp = [3, 4, 1, 5]

def main():
	start = range(256)
	start = range(5)
	skip = 0
	pt = 0
	for el in inp:
		rng_start = pt + skip
		rng_end = pt + skip + el

		# reverse the sublist
		subl = [start[i % len(start)] for i in range(rng_start, rng_end + 1)][::-1]

		start = 

		skip += 1 


if __name__ == '__main__':
	main()