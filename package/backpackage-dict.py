#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def getMaxValueOfPackage(N, C, W, V): # 商品的种类, 背包的容量, 每样商品的容量, 每样商品的价值
	# 构造网格--初始化
	cell = [ [ 0 for i in range(C+1)] for j in range(N+1)]
	for i in range(1, N+1):
		for j in range(1, C+1):
			cell[i][j]=cell[i-1][j]
			if j >= W[i-1] and cell[i][j] < V[i-1] + cell[i-1][j-W[i-1]]:
				cell[i][j] = V[i-1] + cell[i-1][j-W[i-1]]
#	显示网格
	for i in range(N+1):
		print(cell[i])
	return cell

def show(N, C, W, Cell, Goods): # 商品的种类, 背包的容量, 每样商品的容量, 已经规划好的网格, 商品列表
	print('最大价值为:', Cell[N][C])
	processed = [False for i in range(N)]
	cap = C
	for i in range(N, 0, -1):
		if Cell[i][cap] != Cell[i-1][cap]:
			processed[i-1]=True
			cap-=W[i-1]
	print('选择的物品为:', end='')
	for i in range(N):
		if processed[i]:
			print("%s, " % Goods[i], end='')
	print('剩余空间为：', cap)

if __name__ == "__main__":
	capacity = 4
	goods = {}
	goods["吉他"] = [1, 1500]
	goods["音响"] = [4, 3000]
	goods["笔记本"] = [3, 2000]
	goods["IPhone"] = [1, 2000]
	#goods["MP3"] = [1, 1000]

	goods_keys = list(goods.keys()) # 商品列表
	goods_types = len(goods_keys)
	goods_values = list(goods.values()) # 每样商品的容量, 每样商品的价值
	weights = [item[0] for item in goods_values] # 每样商品的容量
	values = [item[1] for item in goods_values] # 每样商品的价值
	print(goods)
	cc = getMaxValueOfPackage(goods_types, capacity, weights, values)
	show(goods_types, capacity, weights, cc, goods_keys)









