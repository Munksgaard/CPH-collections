#!/usr/bin/python
# -*- coding: utf-8 -*-

from fibonacci_priority_queue import *
import unittest

class TestFibonacciNodes(unittest.TestCase):

	def setUp(self):
		self.testnode_values = [5, 10, 20, 50, 3, 100, 58, 42, 7, 36]
		self.nodes = [fibonacci_node(i) for i in self.testnode_values]
	
	def test_insert1(self):
		node5 = fibonacci_node(5)		
		self.assertTrue(node5 == node5.right == node5.left)
	
	def test_insert2(self):
		self.nodes[0].insert(self.nodes[1])
		self.nodes[0].insert(self.nodes[2])
		
		self.assertTrue(self.nodes[0] == self.nodes[0].right.left == self.nodes[0].left.right)
		self.assertTrue(self.nodes[0].right == self.nodes[0].left.left == self.nodes[2])
		self.assertTrue(self.nodes[0].left == self.nodes[0].right.right == self.nodes[1])
		
	def test_iterator1(self):
		tmp = [node for node in self.nodes[0]]
		
		self.assertTrue(len(tmp) == 1)
		self.assertTrue(tmp[0] == self.nodes[0])
		
	def test_iterator2(self):
		for node in self.nodes[1:]:
			self.nodes[0].insert(node)
	
		tmp = []
		for node in self.nodes[0]:
			tmp.append(node)
		
		self.assertTrue(sorted([node.key for node in tmp]) == sorted(self.testnode_values))
		self.assertTrue(tmp[0] == self.nodes[0])
		
		for i in range(1, 10):
			self.assertTrue(tmp[i] == self.nodes[10-i])
		
	def test_concatenate1(self):
		for i in range(1, 5):
			self.nodes[0].insert(self.nodes[i])
			self.nodes[5].insert(self.nodes[5+i])
		self.nodes[0].concatenate(self.nodes[5])
		
		tmp = [node for node in self.nodes[0]]

		self.assertTrue(len(tmp) == 10)	
		self.assertTrue([node for node in tmp if node not in self.nodes] == [])
	
	def test_remove1(self):
		self.nodes[0].insert(self.nodes[1])
		self.nodes[1].remove()
		self.assertTrue(self.nodes[0] == self.nodes[0].right == self.nodes[0].left)
	
	def test_remove2(self):
		self.nodes[0].insert(self.nodes[1])
		self.nodes[0].insert(self.nodes[2])
		self.nodes[2].remove()
		
		self.assertTrue(self.nodes[0] == self.nodes[0].right.right == self.nodes[0].left.left)
		self.assertTrue(self.nodes[1] == self.nodes[1].right.right == self.nodes[1].left.left)
	
	def test_exchange1(self):
		for i in range(1, 5):
			self.nodes[0].insert(self.nodes[i])
			self.nodes[5].insert(self.nodes[5+i])
		
		oldright0 = self.nodes[0].right
		oldleft0 = self.nodes[0].left
		oldright5 = self.nodes[5].right
		oldleft5 = self.nodes[5].left
		
		self.nodes[0].exchange(self.nodes[5])
		
		self.assertTrue(self.nodes[0].right == oldright5 and self.nodes[0].left == oldleft5)
		self.assertTrue(self.nodes[5].right == oldright0 and self.nodes[5].left == oldleft0)
		
class TestFibonacciPriorityQueue(unittest.TestCase):

	def setUp(self):
		self.testnode_values = [5, 10, 20, 50, 3, 100, 58, 42, 7, 36]
		self.nodes = [fibonacci_node(i) for i in self.testnode_values]
		
		self.q = fibonacci_priority_queue()
	
	def test_empty(self):
		self.assertTrue(self.q.is_empty)
		self.assertTrue(self.q.size == 0)
		self.assertTrue(self.q.min == None)
	
	def test_insert1(self):
		self.q.insert(self.nodes[0])
		
		self.assertTrue(self.q.is_empty != True)
		self.assertTrue(self.q.size == 1)
		self.assertTrue(self.q.min == self.nodes[0])
		self.assertTrue(self.q.min.p == None)
		self.assertTrue(self.q.min == self.q.min.right == self.q.min.left)
	
	def test_insert2(self):
		for node in self.nodes[:3]:
			self.q.insert(node)
		
		self.assertTrue(self.q.size == 3)
		self.assertTrue(self.q.min == self.nodes[0])
	
	def test_insert3(self):
		for node in self.nodes:
			self.q.insert(node)
		
		self.assertTrue(self.q.size == len(self.nodes))
		self.assertTrue(self.q.min == self.nodes[4])

	def test_consolidate(self):
		pass
	
	def test_extract_top1(self):
		self.q.insert(self.nodes[0])
		
		node5 = self.q.extract_top()
		
		self.assertTrue(node5 == self.nodes[0])
		self.assertTrue(self.q.size == 0)
		self.assertTrue(self.q.min == None)
	
	def test_extract_top2(self):
		self.q.insert(self.nodes[0])
		self.q.insert(self.nodes[1])
		
		node5 = self.q.extract_top()
		
		self.assertTrue(node5 == self.nodes[0])
		self.assertTrue(self.q.size == 1)
		self.assertTrue(self.q.min == self.nodes[1])
		self.assertTrue(self.q.min == self.q.min.left == self.q.min.right)
	
	def test_extract_top3(self):
		for node in self.nodes:
			self.q.insert(node)
		
		for value in sorted(self.testnode_values):
			tmp = self.q.extract_top()
			if tmp == None:
				break
			print("\n" + str(tmp.key))
			print(value)
			self.assertTrue(tmp.key == value)
			
if __name__=="__main__":
	unittest.main()
