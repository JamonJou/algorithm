#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 旅游行程最优化
r'''假设你要去野营。你有一个容量为6磅的背包,需要决定该携带下面的哪些东西。其中每样东西都有相应的价值,价值越大意味着越重要:
水(重3磅,价值10);
书(重1磅,价值3)
食物(重2磅,价值9);
夹克(重2磅,价值5);
相机(重1磅,价值6)。
请问携带哪些东西时价值最高?
启示》》》
动态规划可帮助你在给定约束条件下找到最优解。在背包问题中,你必须在背包容量给定的情况下,偷到价值最高的商品。
在问题可分解为彼此独立且离散的子问题时,就可使用动态规划来解决。
单元格中的值是什么? 通常就是你要优化的值
如何将这个问题划分为子问题? 限制条件从小到大
网格的坐标轴是什么? x（外循环）可选列表， y（内循环）限制条件
'''
def getMaxValueOfPackage(N, C, W, V): # 名胜的数量, 旅游时间, 每个名胜所花时间, 每个名胜的评分
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

def show(N, C, W, Cell, Goods): # 名胜的数量, 旅游时间, 每个名胜所花时间, 已经规划好的网格, 名胜列表
	print('最大价值为:', Cell[N][C])
	processed = [False for i in range(N)]
	cap = C
	for i in range(N, 0, -1):
		if Cell[i][cap] != Cell[i-1][cap]:
			processed[i-1]=True
			cap-=W[i-1]
	print('选择的地方为:', end='')
	for i in range(N):
		if processed[i]:
			print("%s, " % Goods[i], end='')
	print('剩余时间啊为：', cap)

if __name__ == "__main__":
	days = 4
	monument = {}
	monument["威斯敏斯特教堂"] = [1, 7] # 限制条件， 最大值项
	monument["环球剧场"] = [1, 6]
	monument["英国国家美术馆"] = [2, 9]
	monument["大英博物馆"] = [4, 9]
	monument["圣保罗大教堂"] = [1, 8]

	monument_keys = list(monument.keys()) # 名胜列表
	monument_types = len(monument_keys)
	monument_values = list(monument.values()) # 每个名胜所花时间, 每个名胜的评分
	weights = [item[0] for item in monument_values] # 每个名胜所花时间
	values = [item[1] for item in monument_values] # 每个名胜的评分
	print(monument)
	cc = getMaxValueOfPackage(monument_types, days, weights, values)
	show(monument_types, days, weights, cc, monument_keys)









