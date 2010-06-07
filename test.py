#!/usr/bin/python
# -*- coding: utf-8 -*-

from fibonacci_priority_queue import *

def create_test_values():
      node5 = fibonacci_node(5)
      node10 = fibonacci_node(10)
      node20 = fibonacci_node(20)
      node50 = fibonacci_node(50) 
      test1 = fibonacci_priority_queue()
      test2 = fibonacci_priority_queue() 
      test1.insert(node5)
      test1.insert(node50)
      test2.insert(node10)
      test2.insert(node20) 
      test3 = test1.union(test2)
      return test3

