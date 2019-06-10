#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	货物装箱问题: 每个箱子的尺寸各不相同,你需要尽可能利用每辆卡车的空间,为此你将如何选择要装上卡车的箱子呢?
	已知，货柜尺寸为RR，箱子的尺寸降序为R[1],R[2],...,R[N],其中N表示箱子总数
	求解：满足Q = R[1]+...+R[k] <= RR的最大k
	按照贪婪策略得到的不是最优解，举个栗子：
	RR = 100， R = [50, 40, 30, 20, 5]
	按照贪婪策略：k=2，即 Q = R[1] + R[2] = 50+40 <= 100, R[1]+R[2]+R[3]=120>100
	而最优解应该时R[1]+R[3]+R[4]=50+30+20=100<=100
	类似于背包问题，采用动态规划获取最优解。For i in range(1, RR):更新最大值
'''
'''
	关于旅游，假设每个旅游地的旅游时间以1天为单位，总行程为7天，N个旅游地，对应的价值为V=V[1],V[2],...,V[N],所需天数为T=T[1],T[2],...,T[N]，
	用W = {V[1]:T[1], ... , V[N]:T[N]}
	求解：Q = VMax = V1[1]+...+V1[k] , T1[1]+...+T1[k]<=7, 其中V1[1]---V1[k]为V的子集，T1[1]---T1[k]为对应的T子集, W1 = {V1[1]:T1[1], ... , V1[k]:T1[k]}为W的子集
'''
'''
	集合覆盖问题：假设你办了个广播节目,要让N个州的听众都收听得到。为此,你需要决定在哪些州广播台播出。在尽可能少的广播台播出。每个广播台都覆盖特定的区域（州）,不同广播台的覆盖区域可能重叠。
	1. 选出这样一个广播台,即它覆盖了最多的未覆盖州。
	2. 重复第一步，直到覆盖所有的州
	采用贪婪策略获得近似解
'''
# 背包的容量 capacity
capacity = 4

# 商品的重量和价值
goods = ["音响", "吉他", "笔记本"]
weights = [4, 1, 3]
values = [3000, 1500, 2000]

# 商品的种类数 types
types = len(goods)

def dynamicPlan():
	cell = [ [0 for j in range(capacity+1)] for i in range(types+1) ]
	#for i in range(types+1):
	#	cell[0][i]=0

	for i in range(1, types+1):
		for j in range(1, capacity+1):
			cell[i][j] = cell[i-1][j]
			if j >= weights[i-1] and values[i-1]+cell[i-1][j-weights[i-1]] > cell[i][j]:
				cell[i][j]=values[i-1]+cell[i-1][j-weights[i-1]]
#	显示网格
	for i in range(types+1):
		print(cell[i])
	return cell

def pathTrace(cell):
	processed=[False for i in range(types)]
	cap = capacity
	for i in range(types, 0, -1):
		if cell[i][cap] != cell[i-1][cap]:
			processed[i-1]=True
			cap-=weights[i-1]
	print(processed)
	print("You choose goods:", end='')
	for i in range(1, types+1):
		if processed[i-1]:
			print("%s, " % goods[i-1], end='')
	print()

if __name__ == "__main__":
	pathTrace(dynamicPlan())
	
