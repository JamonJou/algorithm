#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 背包的容量
capacity = 4
# 商品的种类
types = 3
# 每样商品的容量
#weights = [3, 4, 1]
# 对应的每样商品的价值
#values = [2000, 3000, 1500]
#weights = [4, 1, 3]
#values = [3000, 1500, 2000]
def getMaxValueOfPackage():
	cell = [[ 0 for i in range(capacity+1)] for j in range(types+1)]
	print(cell)
	for j in range(types+1):
		cell[0][j]=0
	for i in range(1, types+1):
		for j in range(1, capacity+1):
			cell[i][j] = cell[i-1][j];
			if j>= weights[i-1] and cell[i][j] < values[i-1]+cell[i-1][j-weights[i-1]]:
				cell[i][j] = values[i-1]+cell[i-1][j-weights[i-1]]
	print(cell)
	return cell

def show(n,c,w,res):
	print('最大价值为:',res[n][c])
	x=[False for i in range(n)]
	j=c
	for i in range(n, 0, -1):
		if res[i][j]!=res[i-1][j]:
			x[i-1]=True
			j-=w[i-1]
	print('选择的物品为:')
	for i in range(n):
		if x[i]:
			print('第',i,'个,',end='')
	print('')

if __name__ == "__main__":
	show(types, capacity, weights, getMaxValueOfPackage())




















