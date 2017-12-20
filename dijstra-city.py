#! /usr/bin/env python3
# -*- coding: utf-8 -*-

graph = {}

graph["起点"] = {}
graph["起点"]["武汉"] = 5
graph["起点"]["岳阳"] = 2

graph["武汉"] = {}
graph["武汉"]["长沙"] = 4
graph["武汉"]["广州"] = 2

graph["岳阳"] = {}
graph["岳阳"]["武汉"] = 8
graph["岳阳"]["广州"] = 7

graph["长沙"] = {}
graph["长沙"]["深圳"] = 3
graph["长沙"]["广州"] = 6

graph["广州"] = {}
graph["广州"]["深圳"] = 1

graph["深圳"] = {}

infinity = float("inf")
costs = {}
costs["起点"] = 0
costs["武汉"] = infinity
costs["岳阳"] = infinity
costs["广州"] = infinity
costs["长沙"] = infinity
costs["深圳"] = infinity

parents = {}
parents["武汉"] = "起点"
parents["岳阳"] = "起点"
parents["深圳"] = None

processed = []
path = []

def find_lowest_cost_node(tb_costs):
	lowest = infinity
	lowest_node = None
	for node in tb_costs:
		cc = costs[node]
		if cc < lowest and node not in processed:
			lowest = cc
			lowest_node = node
	return lowest_node

def dijkstra():
	node = find_lowest_cost_node(costs)
	while node is not None:
		path.append(node)
		cost = costs[node]
		neighbors = graph[node]
		for i in neighbors.keys():
			new_cost = cost + neighbors[i]
			if new_cost < costs[i]:
				costs[i] = new_cost
				parents[i] = node
			elif node in path:
				path.remove(node)
		processed.append(node)
		node = find_lowest_cost_node(costs)

if __name__ == "__main__":
	dijkstra()
	print(costs["深圳"])
	print(costs)
	print(path)
