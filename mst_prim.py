#!/usr/bin/python
# -*- coding: utf-8 -*-

import heapq

class node(object):
	pass

def mst_prim_heapq():
	V = [node() for i in range(100)]
	
	r = V[0]
	
	for u in V:
		u.key = 999999
		u.p = None
	
	r.key = 0
	
	

def main():
	mst_prim_heapq()

if __name__=="__main__":
	main()
