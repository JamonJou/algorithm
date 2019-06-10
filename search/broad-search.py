#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
graph = {}

graph['A'] = ['B', 'F']
graph['B'] = ['C']
graph['C'] = ['D']
graph['F'] = ['E', 'G']
graph['E'] = ['C']
#graph['E'] = []
graph['G'] = ['C']
graph['D'] = []
def broadsearch(start, target):
	search_queue = deque()
	search_queue += graph[start]
	got = False
	searched = []
	while search_queue:
		node = search_queue.popleft()
		if node not in searched:
			print(node)
			if node == target:
				#print("Found it!")
				got = True
			else:
				search_queue += graph[node]
				searched.append(node)
	print("Process is" + str(searched))
	return got
if __name__ == "__main__":
	getprocess = broadsearch('A', 'D')
	if getprocess:
		print("Found it")
	else:
		print("Not Found it")
































	
