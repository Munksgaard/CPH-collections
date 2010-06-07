#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This abstract base class is an adaptation of meldable_priority_queue
from the CPH STL. 

Copyright: Jyrki Katajainen © 2010
"""

import abc
from free_functions import *

class meldable_priority_queue(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod  
  def __init__(self, comparator = lambda x, y: x < y, collection = None, 
               iterator = None): 
    """Create a meldable-priority-queue object; 
    comparator is a function used in element comparisons;
    collection is an iterable object used to populate self;
    iterator is an object used to perform iteration"""
    self._comparator = comparator
    self.size = 0

    if collection != None:
      for element in collection:
        insert(self, element)
    self._iterator = iterator

  @abc.abstractmethod  
  def __del__(self):
    "Destroy an instance"
    pass

  @abc.abstractmethod  
  def __repr__(self):
    "Create a full string representation of an object"
    pass

  @abc.abstractmethod
  def __str__(self):
    "Create an informal string representation"
    pass

  def __nonzero__(self):
    "Return 0 or 1 for truth-value testing"
    return int(self.size != 0)

  def __len__(self):
    "Return the length of self"
    return self.size

  def get_comparator(self):
    "Return the comparator object"
    return self._comparator

  comparator = abc.abstractproperty(get_comparator)

  def __iter__(self):
    "Return the iterator object"
    return self._iterator

  def set_iterator(self, iterator):
    "Update the iterator object"
    self._iterator = iterator

  iterator = abc.abstractproperty(__iter__, set_iterator)

  @abc.abstractmethod
  def get_size(self):
    "Return the number of elements stored in self"  
    pass

  size = abc.abstractproperty(get_size)

  def get_is_empty(self):
    "Return True if self.size == 0; otherwise return False"
    return self.size == 0

  is_empty = abc.abstractproperty(get_is_empty)

  def clear(self):
    "Remove all elements from self"
    while not self.is_empty:
      extract(self)

  @abc.abstractmethod
  def swap(self, other):
    "Swap the contents of self and other"
    pass

  @abc.abstractmethod
  def find_top(self):
    "Return the encapsulator containing the top element of self"
    return 

  @abc.abstractproperty
  def top(self):
    "Return the top element of self"
    pass

  @abc.abstractmethod
  def insert(self, x):
    "Add element x to self and return its encapsulator"
    pass

  def extract_top(self):
    "Remove the encapsulator containing the top element from self"
    erase(self, find_top(self))

  @abc.abstractmethod
  def extract(self):
    "Remove an unspecified encapsulator together with its element from self"
    pass

  @abc.abstractmethod
  def erase(self, encapsulator):
    "Remove the given encapsulator together with its element from self"
    pass

  @abc.abstractmethod
  def increase(self, encapsulator, element):
    "Increase the value of the element at the given encapsulator in self"
    pass

  @abc.abstractmethod
  def union(self, other):
    "Take the union of self and other, and destroy their previous contents"
    pass
