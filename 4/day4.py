# https://adventofcode.com/2017/day/4

__author__ = 'Remus Knowles <remknowles@gmail.com>'

from math import factorial

def anagram(word1,word2):
	return sorted(word1) == sorted(word2)

def load():
	"""
	Read in word list.
	"""
	cnt = 0
	with open(r"in.txt", 'r') as f:
		for r in f:
			words = r.replace('\n','').split()
			words = [''.join(sorted(w)) for w in words]
			if len(words) == len(set(words)):
				cnt += 1
	return cnt

def main():
	print load()

if __name__ == '__main__':
	main()