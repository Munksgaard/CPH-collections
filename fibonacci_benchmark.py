#!/usr/bin/python
# -*- coding: utf-8 -*-

from fibonacci_priority_queue import *
from random import sample

def fibonacci_benchmark(keys):
	queue = fibonacci_priority_queue()
	
	for key in keys:
		queue.insert(fibonacci_node(key))
	
	while queue.extract_top() != None:
		pass
	
def main():
	keys = sample(list(range(1, 20000)), 10000)
	fibonacci_benchmark(keys)
	
if __name__=="__main__":
	main()
