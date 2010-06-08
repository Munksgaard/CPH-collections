#!/usr/bin/python
# -*- coding: utf-8 -*-

from meldable_priority_queue import meldable_priority_queue
from math import log

class fibonacci_node(object):
	def __init__(self, key):
		self.key = key
		self.degree = 0
		self.p = None
		self.child = None
		self.mark = False
		self.right = self.left = self
		
	def __iter__(self):
		count = 1
		next = self.right
		while next != self:
			count += 1
			next = next.right
			
		self.items = []
		item = self
		for i in range(count):
			self.items.append(item)
			item = item.right
		
		return iter(self.items)
	
	def insert(self, x):
		x.left = self
		x.right = self.right
		x.right.left = x
		x.left.right = x
		
	def concatenate(self, other):
		oldleft = self.left
		self.left = other.min
		other.min.right.left = oldleft
		oldleft.right = other.min.right
		other.min.right = self
		
	def remove(self):
		""" Removes the node from the list its in.
		Only works if its not the only node in the list."""
		self.right.left = self.left
		self.left.right = self.right
		
	def exchange(self, other):
		oldright = self.right
		oldleft = self.left
		
		self.right = other.right
		other.right = oldright
		
		self.left = other.left
		other.left = oldleft
		

class fibonacci_priority_queue():

	def __init__(self, comparator = lambda x, y: x < y, collection = None, iterator = None):
		self.min = None
		meldable_priority_queue.__init__(self, comparator, collection, iterator)
		
	def __iter__(self):
		return self
		
	def __del__(self):
		self.min = None

	def insert(self, x):
		x.degree = 0
		x.p = None
		x.child = None
		x.mark = False

		if self.min == None:
			# create a root list for self containing just x
			self.min = x
		else:
			# insert x to the root list of self
			self.min.insert(x)
			if x.key < self.min.key:
				self.min = x
		self.size += 1

	def union(self, other):
		# concatenate the root list of other to self
		self.min.concatenate(other)
		if self.min == None or (other.min != None and other.min.key < self.min.key):
			self.min = other.min
		self.size += other.size
		return self
		
	def D(self):
		return log(self.size, 2)
		
	def erase(self, encapsulator):
		pass #mangler
		
	def consolidate(self):
		A = [None for x in range(int(self.D()) + 1)]

		for w in self.min:			
			x = w
			d = x.degree
			while A[d] != None:
				y = A[d]
				if x.key > y.key:
					x.exchange(y)
				self.heap_link(y, x)
				A[d] = None
				d += 1
			A[d] = x
				
		self.min = None
		
		for i in range(int(self.D()) + 1):
			if A[i] != None:
				if self.min == None:
					# create a root list for self containing just A[i]
					self.min = A[i]
					A[i].right = A[i].left = A[i]
				else:
					#insert A[i] H's root list
					self.min.insert(A[i])
					if A[i].key < self.min.key:
						self.min = A[i]
		
	def heap_link(self, y, x):
		#remove y from the root list of H
		y.remove()
		
		#make y a child of x, incrementing x.degree
		if x.child == None:
			y.right = y
			y.left = y
		else:
			x.child.insert(y)
		x.child = y
		y.p = x
		x.degree += 1
		
		y.mark = False
		
	def extract_top(self):
		z = self.min
		if z != None:
			if z.child != None:
				for x in z.child:
					self.min.insert(x)
					x.p = None
					
			z.remove()
			if z == z.right:
				self.min = None
			else:
				self.min = z.right
				self.consolidate()
			self.size -= 1
		return z
	
	def find_top(self):
		return self.min
				
	def cut(self, x, y):
		if x.right != x:
			x.remove()
		y.degree -= 1
		self.min.insert(x)
		x.p = None
		x.mark = False
			
	def cascading_cut(self, y):
		z = y.p
		if z != None:
			if y.mark == False:
				y.mark = True
			else:
				self.cut(y, z)
				self.cascading_cut(z)
				
	def decrease_key(self, x, k):
		if k > x.key:
			raise Exception("New key is greater than current key")
		x.key = k
		y = x.p
		if y != None and x.key < y.key:
			self.cut(x, y)
			self.cascading_cut(y)
		if x.key < self.min.key:
			self.min = x
			
	def delete(self, x):
		self.decrease_key(x, self.min.key - 1)
		self.extract_top()
		
meldable_priority_queue.register(fibonacci_priority_queue)
