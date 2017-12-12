# https://adventofcode.com/2017/day/9 

__author__ = 'Remus Knowles <remknowles@gmail.com>'

import re

def discard_cancelled(string):
	"""
	Get rid of any cancelled chars in the string.
	"""

	return re.sub(r'\!.','',string)

def discard_garbage(string, garbage_counted):
	"""
	Parse out any garbage from the strings and return only { and } chars.
	"""

	if not '<' in string:
		return string, 0

	for i, c in enumerate(string):
		if c == '<':
			start = i
			for j, c2 in enumerate(string[start:]):
				if c2 == '>':
					end = start + j
					garbage_counted += end - start - 1
					print garbage_counted
					return discard_garbage(string[:start] + string[end+1:], garbage_counted)

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

	clean, garbage_counted = discard_garbage(discard_cancelled(txt),0)
	print garbage_counted

if __name__ == '__main__':
	main()