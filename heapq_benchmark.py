#!/usr/bin/python
# -*- coding: utf-8 -*-

from heapq import *
from random import sample

def heapq_benchmark(keys):
	queue = []
	heapify(queue)
	
	for key in keys:
		heappush(queue, key)
	
	try:
		while heappop(queue):
			pass
	except IndexError:
		pass
	
#	print("Heapq done!")

def main():
	keys = sample(list(range(1, 20000)), 10000)
	heapq_benchmark(keys)

if __name__=="__main__":
	main()
