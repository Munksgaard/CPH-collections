#!/usr/bin/python
# -*- coding: utf-8 -*-

from fibonacci_priority_queue import *
from heapq import *
from random import sample

def fibonacci_benchmark(keys):
	queue = fibonacci_priority_queue()
	heap = []
	
	print(sorted(keys))
	
	for key in keys:
		queue.insert(fibonacci_node(key))
		heappush(heap, key)
	
	
	for i in range(100):
		print("Next")
		print(queue.extract_top().key)
		print(heappop(heap))

	print("Fibonacci done!")
	
def main():
	keys = sample(list(range(1, 1000)), 500)
	fibonacci_benchmark(keys)
	
if __name__=="__main__":
	main()
