# 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

inp = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'
test = '0	2	7	0'

def main():
	start = [int(x) for x in inp.split('\t')]

	states = []
	cur = start
	cnt = 0

	while not cur in states:
		cnt += 1
		cp = cur[:]
		states.append(cp)

		n = max(cur)
		i = cur.index(n)
		cur[cur.index(n)] = 0
		for _ in range(n):
			i += 1
			j = i % len(cur)
			cur[j] += 1

	print len(states) - states.index(cur)

if __name__ == '__main__':
	main()