# https://adventofcode.com/2017/day/5

__author__ = 'Remus Knowles <remknowles@gmail.com>'

# stack = [0,3,0,1,-3]

def main():

	with open('ins.txt') as f:
		stack = [int(x) for x in f]

	pnt = 0
	count = 0
	while 0 <= pnt < len(stack):
		count += 1
		jmp = stack[pnt]
		stack[pnt] += 1
		pnt += jmp


	print count

if __name__ == '__main__':
	main()