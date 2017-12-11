# https://adventofcode.com/2017/day/9 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

def discard_garbage(string):
	"""
	Parese out any garbage from the strings and return only { and } chars.
	"""

	if not '<' in string:
		return string

	for i, c in enumerate(string):
		if c == '<':
			start = i
			for j, c2 in enumerate(string[start:]):
				if c2 == '>':
					cancel_cnt = 0
					
					for el in string[::-1][-start-j:-start-1]:
						if el == '!':
							cancel_cnt += 1
						else:
							break

					if cancel_cnt % 2 == 0:
						end = start + j
						return discard_garbage(string[:start] + string[end+1:])
					else:
						continue

def value(string):
	"""
	Work out the score for a string of { and }.
	"""

	s = 0
	val = 0

	for c in string:
		if c == '{':
			val += 1
		elif c == '}':
			s += val
			val -= 1

	return s

def main():
	with open('in.txt') as f:
		txt = f.read()

	# txt = '{{<!!!>>}}'

	print value(discard_garbage(txt))

if __name__ == '__main__':
	main()