#! /usr/bin/env python3
# -*- coding: utf-8 -*-

''' Dijstra just relate to directed acyclic graph'''
DAGraph = {}
DAGraph['S'] = {}
DAGraph['A'] = {}
DAGraph['B'] = {}
DAGraph['E'] = {}

DAGraph['S']['A'] = 6
DAGraph['S']['B'] = 2
DAGraph['B']['A'] = 3
DAGraph['B']['E'] = 5
DAGraph['A']['E'] = 1

infinity = float("inf")
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['E'] = infinity

parents = {}
parents['A'] = 'S'
parents['B'] = 'S'
parents['E'] = None

processed = []

def find_lowest_cost_node(tb_costs):
	lowest = float("inf")
	lowest_node = None
	for node in tb_costs:
		cc = costs[node]
		if cc < lowest and node not in processed:
			lowest = cc
			lowest_node = node
	return lowest_node

def dijstra():
	# choose 
	node = find_lowest_cost_node(costs)
	while node is not None:
		cost = costs[node]
		neighbors = DAGraph[node]
		for n in neighbors.keys():
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost:
				costs[n] = new_cost
				parents[n] = node
		# update and flag
		processed.append(node)
		# loop
		node = find_lowest_cost_node(costs)

if __name__ == "__main__":
	dijstra()
	print(costs['E'])

