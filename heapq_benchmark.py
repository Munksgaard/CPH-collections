#!/usr/bin/python
# -*- coding: utf-8 -*-

from heapq import *

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
	
	print("Heapq done!")
