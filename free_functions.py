#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
These functions work for all collections, provided that the collection
in question has the attributes required. The full specification of
most of these functions can be found from the C++ standard
(standardization document N3092).

Copyright: Jyrki Katajainen © 2010

Disclaimer: Many simple, but useful, functions are still missing.
"""

def equal_to(object, other):
  "Return True if object == other"
  if hasattr(object, "__eq__") and type(other) is type(object):
    return object.__eq__(other)
  if hasattr(other, "__lt__") and type(other) is type(object):
    return (not object.__lt__(other)) and (not other.__lt__(object))
  raise AttributeError

def less(object, other):
  "Return True if object < other"
  if hasattr(object, "__lt__") and type(other) is type(object):
    return object.__lt__(other)
  raise AttributeError

def adjacent_find(collection, comparator = equal_to):
  """Return the first encapsulator in collection whose element compares
  equal to that stored in its adjacent neighbour"""
  raise NotImplemented

def append(collection, x):
  "Append element x to the end of collection"
  if hasattr(collection, "push_back"):
    collection.push_back(x)
    return
  if hasattr(collection, "push"):
    collection.push(x)
    return
  raise AttributeError

def assign(collection, other):
  "Assign the contents of other to collection"
  clear(collection)
  extend(collection, other)

def binary_search(collection, element, comparator = less):
  "Return True if element is in the given sorted collection"
  raise NotImplemented

def clear(collection):
  "Remove all elements from collection"
  if hasattr(collection, "clear"):
    return collection.clear()
  raise AttributeError

def count(collection, element):
  "Return the number of times element appears in collection"
  if hasattr(collection, "count"):
    return collection.count()
  if not hasattr(collection, "__iter__"):
    raise AttributeError
  n = 0
  for x in collection:
    if equal_to(element, x):
      n += 1
  return n

def count_if(collection, predicate):
  "Return the number of elements in collection that satisfy predicate"
  if not hasattr(collection, "__iter__"):
    raise AttributeError
  n = 0
  for x in collection:
    if predicate(x):
      n += 1
  return n

def difference(collection, other, result, comparator = less):
  "Compute the difference of two sets in normal set-theoretic sense"
  raise NotImplemented

def extend(collection, other):
  "Append the elements of other to the end of collection"
  if hasattr(collection, "push_back"):
    for element in other:
      collection.push_back(element)
    return
  if hasattr(collection, "push"):
    for element in other:
      collection.push(element)
    return
  raise AttributeError

def find(collection, element):
  "Return the first encapsulator in collection containing the given element"
  raise NotImplemented

def find_if(collection, predicate):
  """Return the first encapsulator in collection containing an element
  for which predicate is True"""
  raise NotImplemented

def get_back(collection):
  "Return the last element of collection"
  if hasattr(collection, "get_back"):
    return collection.get_back()
  if hasattr(collection, "get_top"):
    return collection.get_top()
  raise AttributeError

def get_capacity(collection):
  "Return the capacity of collection"  
  if hasattr(collection, "get_capacity"):
    return collection.get_capacity()
  raise AttributeError

def get_comparator(collection):
  "Return the comparator object of collection"
  if hasattr(collection, "get_comparator"):
    return collection.get_comparator()
  raise AttributeError

def get_extractor(collection):
  "Return the extractor object of collection"
  if hasattr(collection, "get_extractor"):
    return collection.get_extractor()
  raise AttributeError

def get_front(collection):
  "Return the first element of collection"
  if hasattr(collection, "get_front"):
    return collection.get_front()
  raise AttributeError

def get_is_empty(collection):
  "Return True if the size of collection is 0; otherwise return False"
  if hasattr(collection, "get_is_empty"):
    return collection.get_is_empty()
  raise AttributeError

def get_iterator(collection):
  "Return the iterator object of collection"
  if hasattr(collection, "__iter__"):
    return collection.__iter__()
  raise AttributeError

def get_size(collection):
  "Return the number of elements stored in collection"  
  if hasattr(collection, "get_size"):
    return collection.get_size()
  raise AttributeError

def greater(object, other):
  "Return True if object > other"
  less(other, object)

def greater_equal(object, other):
  "Return True if object >= other"
  return not less(object, other)

def includes(collection, other, comparator = less):
  "Test whether every element in other has a counterpart in collection, or not"
  raise NotImplemented

def index(collection, x):
  """Return the index of the first element in collection whose value is x;
  it is an error if there is no such element"""
  if not hasattr(collection, "__iter__"):
    raise AttributeError
  n = 0
  for y in collection:
    if x == y:
      return n
    n += 1      
  raise ValueError

def inplace_merge(collection, other, comparator = less):
  """Combine two consecutive sorted collections into a single sorted
  collection; when doing this use only O(1) extra space"""
  raise NotImplemented

def inplace_sort(collection, comparator = less, extractor = None):
  """Sort the elements of collection, in place; comparator tells how
  elements are compared and extractor which part of elements is used
  in comparisons"""
  raise NotImplemented

def intersection(collection, other, result, comparator = less):
  "Compute the intersection of two sets in normal set-theoretic sense"
  raise NotImplemented

def less_equal(object, other):
  "Return True if object <= other"
  return not less(other, object)

def lower_bound(collection, element, comparator = less):
  "Return the first encapsulator in collection containing the given element"
  raise NotImplemented

def make_heap(collection, comparator = less):
  "Turn an arbitrary collection into a heap"
  raise NotImplemented

def merge(collection, other, result, comparator = less):
  "Combine two sorted collections into a single sorted collection"
  raise NotImplemented

def next_permutation(collection, comparator = less):
  """Transform the given collection of elements into the
  lexicographically next greater permutation of these elements"""
  raise NotImplemented

def not_equal(object, other):
  "Return True if object != other"
  return not equal(object, other)

def partial_sort(collection, k, comparator = less, extractor = None):
  """Rearrange the elements of collection such that the k smallest of
  them are sorted in ascending order with respect to comparator;
  extractor tells which part of elements is used in comparisons"""
  raise NotImplemented

def pop_back(collection):
  "Remove the last element of collection"
  if hasattr(collection, "pop_back"):
    collection.pop_back()
    return
  if hasattr(collection, "pop"):
    collection.pop()
    return
  raise AttributeError

def pop_front(collection):
  "Remove the first element of collection"
  if hasattr(collection, "pop_front"):
    collection.pop_front()
    return
  raise AttributeError

def pop_heap(collection, comparator = less):
  "Remove the top element from the heap by placing it at the end of collection"
  raise NotImplemented

def prev_permutation(collection, comparator = less):
  """Transform the given collection of elements into the
  lexicographically next smaller permutation of these elements"""
  raise NotImplemented

def push_back(collection, x):
  "Append element x to the end of collection"
  if hasattr(collection, "push_back"):
    collection.push_back(x)
    return
  if hasattr(collection, "push"):
    collection.push(x)
    return
  raise AttributeError

def push_front(collection, x):
  "Append element x to the beginning of collection"
  if not hasattr(collection, "push_front"):
    raise AttributeError
  collection.push_front(x)

def push_heap(collection, comparator = less):
  "Add the last element to a heap"
  raise NotImplemented

import random

def random_shuffle(collection, generator = random.SystemRandom):
  """Rearrange collection randomly, in place, using generator to
  obtain random numbers"""
  raise NotImplemented

def random_sample(collection, result, generator = random.SystemRandom):
  """Copy a sample of the elements from collection to result using
  generator to obtain random numbers"""
  raise NotImplemented

def remove(collection, x):
  """Remove the first element from collection whose value is equal to x;
  it is an error if there is no such element"""
  raise NotImplemented

def remove_if(collection, predicate):
  """Remove the first element from collection for which the predicate is True;
  it is an error if there is no such element"""
  raise NotImplemented

def reverse(collection):
  "Reverse the elements of collection, in place"
  raise NotImplemented

def reverse_copy(collection, result):
  "Reverse the elements of collection by copying them to result"
  raise NotImplemented

def rotate(collection, n):
  "Rotate the elements of collection, in place, n positions to the right"
  raise NotImplemented

def rotate_copy(collection, n, result):
  """Rotate the elements of collection n positions to the right by
  producing the output to result"""
  raise NotImplemented

def search(collection, other, comparator = equal_to):
  """Search for the first appearance of other in collection using
  comparator to determine whether two elements are the same"""
  raise NotImplemented

def search_end(collection, other, comparator = equal_to):
  """Search for the last appearance of other in collection using
  comparator to determine whether two elements are the same"""
  raise NotImplemented

def set_back(collection, x):
  "Update the last element of collection to be x"  
  if hasattr(collection, "set_back"):
    return collection.set_back(x)
  if hasattr(collection, "set_top"):
    return collection.set_top(x)
  raise AttributeError

def set_capacity(collection, n):
  "Set the capacity of collection to n"  
  if hasattr(collection, "set_capacity") and type(n) is int:
    return collection.set_capacity(n)
  raise AttributeError

def set_front(collection, x):
  "Update the first element of collection to be x"  
  if hasattr(collection, "set_front"):
    return collection.set_front(x)
  raise AttributeError

def set_iterator(collection, iterator):
  "Update the iterator object of collection"  
  if hasattr(collection, "set_iterator") and hasattr(iterator, "__iter__"):
    return collection.set_iterator(iterator)
  raise AttributeError

def set_size(collection, n):
  "Set the size of collection to n"  
  if hasattr(collection, "set_size") and type(n) is int:
    return collection.set_size(n)
  raise AttributeError

def symmetric_difference(collection, other, result, comparator = less):
  "Compute the symmetric difference of two sets in normal set-theoretic sense"
  raise NotImplemented

def sort(collection, comparator = less, extractor = None):
  """Sort the elements of collection; comparator tells how elements
  are compared and extractor which part of elements is used in
  comparisons"""
  raise NotImplemented

def sort_heap(collection, comparator = less):
  "Convert a heap into a sorted collection"
  raise NotImplemented

def swap(collection, other):
  "Swap the contents of collection and other"
  if hasattr(collection, "swap") and type(other) is type(collection):
    return collection.swap(other)
  raise AttributeError

def union(collection, other, result, comparator = less):
  "Compute the union of two sets in normal set-theoretic sense"
  raise NotImplemented

def unique(collection, comparator = equal_to):
  "Eliminate duplicates from every consecutive group of equal elements"
  raise NotImplemented

def upper_bound(collection, element, comparator = less):
  """Return the first encapsulator in collection where element could
  be placed without violating the ordering"""
  raise NotImplemented

