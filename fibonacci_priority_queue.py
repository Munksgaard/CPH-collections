#!/usr/bin/python
# -*- coding: utf-8 -*-

from meldable_priority_queue import *
from math import log

class fibonacci_node(object):
	def __init__(self, key, element = None):
		self.key = key
		self.degree = 0
		self.p = None
		self.child = None
		self.mark = False
		self.right = self.left = self
		self.element = element
		
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
		oldright = self.right
		self.right = other
		other.left.right = oldright
		oldright.left = other.left
		other.left = self
		
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
		

class fibonacci_priority_queue(meldable_priority_queue):

	def __init__(self, comparator = lambda x, y: x < y, collection = None, iterator = None):
		self._comparator = comparator
		self.__size = 0

		if collection != None:
			for element in collection:
				insert(self, element)
		self._iterator = iterator
		self.min = None
		
	def __del__(self):
		self.min = None
		
	def __repr__(self):
		return object.__repr__(self)
	
	def __str__(self):
		return self.__repr__()
		
	comparator = property(get_comparator)
	
	# Overwrites the API function
	def __iter__(self):
		return self
		
	iterator = property(__iter__, set_iterator)
	
	def get_size(self):
		return self.__size
	
	size = property(get_size)
	
	is_empty = property(get_is_empty)
	
	# INCOMPLETE
	def swap(self, other):
		tmp = other
		other = self
		self = tmp

	def find_top(self):
		return self.min
	
	def top(self):
		pass # INCOMPLETE

	def insert(self, x):
		x.degree = 0
		x.p = None
		x.child = None
		x.mark = False

		if self.min == None:
			# create a root list for self containing just x
			self.min = x
			self.min.right = self.min
			self.min.left = self.min
		else:
			# insert x to the root list of self
			self.min.insert(x)
			if x.key < self.min.key:
				self.min = x
		self.__size += 1	

	# Overwrites the API method
	def extract_top(self):	
		z = self.min
		if z != None:
			if z.child != None:
				for x in z.child:
					self.min.insert(x)
					x.p = None
				for node in z:
					print(node.key)
			z.remove()
			if z == z.right:
				self.min = None
			else:
				self.min = z.right
				self.consolidate()
			self.__size -= 1
		return z
	
	# Helper-function for extract_top
	def consolidate(self):
		A = [None for x in range(int(self.__D()) + 1)]

		for w in self.min:			
			x = w
			d = x.degree
			while A[d] != None:
				y = A[d]
				if x.key > y.key:
					x.exchange(y)
				self.__heap_link(y, x)
				A[d] = None
				d += 1
			A[d] = x
		
		self.min = None

		for i in range(int(self.__D()) + 1):
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
						
	# Helper-function for __consolidate
	# Returns the max number of elements in the root list.
	def __D(self):
		return log(self.__size, 2)
		
	# Helper-function for __consolidate
	def __heap_link(self, y, x):
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
		
	def extract(self, encapsulator):
		pass # UNIMPLEMENTED
	
	def erase(self, encapsulator):
		pass # UNIMPLEMENTED
	
	def increase(self, encapsulator, element):
		pass # UNIMPLEMENTED
	
	def union(self, other):
		# concatenate the root list of other to self
		self.min.concatenate(other.min)
		if self.min == None or (other.min != None and other.min.key < self.min.key):
			self.min = other.min
		self.__size += other.get_size
		return self
				
	def decrease_key(self, x, k):
		if k > x.key:
			raise Exception("New key is greater than current key")
		x.key = k
		y = x.p
		if y != None and x.key < y.key:
			self.__cut(x, y)
			self.__cascading_cut(y)
		if x.key < self.min.key:
			self.min = x
	
	# Helper-function for decrease_key
	def __cut(self, x, y):
		if x.right != x:
			x.remove()
		else:
			y.child = None
		y.degree -= 1
		self.min.insert(x)
		x.p = None
		x.mark = False

	# Helper-function for decrease_key
	def __cascading_cut(self, y):
		z = y.p
		if z != None:
			if y.mark == False:
				y.mark = True
			else:
				self.__cut(y, z)
				self.__cascading_cut(z)
			
	def delete(self, x):
		self.decrease_key(x, self.min.key - 1)
		self.extract_top()
		
