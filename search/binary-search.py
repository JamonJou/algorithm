#! /usr/bin/env python3
# -*- coding: utf-8 -*-

alist = [13, 20, 5, 89, 30, 80, 1, 3]
alist.sort()
def binary_search(alist, near):
	low = 0
	high = len(alist) - 1
	while low <= high:
		medium = (low + high) // 2
		guess = alist[medium]
		if guess == near:
			return medium;
		elif guess < near:
			low = medium + 1
		elif guess > near:
			high = medium -1
	return None
'''
	if(high < low):
		return medium;
	if near == alist[medium] :
		return medium
	elif near < alist[medium] :
		return binary_search(alist[low:medium], near)
	else :
		return binary_search(alist[medium:high], near)
'''

if __name__ == "__main__":
	target = 20
	local = binary_search(alist, target)
	print(" target = %d , local at alist[%d]" % (target, local))

def caipiao(N):
	import random
	random.sample(range(1,34), 6)
	random.sample(range(1,17), 1)

class Singleton(object):
	__instance = None
	def __init__(self):
		pass
	def __new__(cls, *args, **kawargs):
		if not cls.__instance:
			cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls.__instance



