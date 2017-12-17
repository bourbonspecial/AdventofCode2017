# https://adventofcode.com/2017/day/13

__author__ = 'Remus Knowles <remknowles@gmail.com>'

test = [3,2,0,0,4,0,4]

def parse():
	with open('in.txt') as f:
		pairs = [(int(r.split(': ')[0]), int(r.split(': ')[1]))  for r in f]

	maxi = max([p[0] for p in pairs])

	fwall = [0 for _ in range(maxi+1)]

	for i, v in pairs:
		fwall[i] = v

	return fwall

def main():
	fwall = parse()
	# fwall = test
	ps = 0
	pt = -1
	severity = 0

	while pt < len(fwall) - 1:
		pt += 1

		if ps % ((fwall[pt] - 1) * 2) == 0:
			severity += pt * fwall[pt]

		ps += 1

	print severity

if __name__ == '__main__':
	main()