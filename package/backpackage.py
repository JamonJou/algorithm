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
capacity = 4
goods = {}
goods["吉他"] = [1, 1500]
goods["音响"] = [4, 3000]
goods["笔记本"] = [3, 2000]

values = []
weights = []

processed_goods = []
choosed_goods = []

maxValue = 0

def getMaxValueOfPackage():

	cell = []
	keys = list(goods.keys())
	values = list(goods.values())

	for i in range(len(keys)):
		inner = []
		for j in range(capacity):
			# 当前商品的价值和容量
			cur_goods_value = values[i][1]
			cur_goods_cap = values[i][0]
			# 当前容量
			cur_cap = j + 1
			# 如果放入，那么当前剩余空间
			left_cap = cur_cap - cur_goods_cap
			print("cur_goods_value = %d, cur_goods_cap = %d, cur_cap = %d, left_cap = %d" % (cur_goods_value, cur_goods_cap, cur_cap, left_cap), end='\t')
			if i == 0:#第一轮
				if ( cur_goods_cap <= cur_cap ):#如果放得下
					inner.append(cur_goods_value)
				else:
					inner.append(0)
				cell.append(inner)
			else:#第二轮,,,,
				#如果放得下
				if( 0 <= left_cap ):
					k = 0
					left_value = 0 # 剩余空间的价值
					while(k<=i):
						if values[k][0] <= left_cap:
							left_value = values[k][1]
						k=k+1
					# 如果放入，并且没有超过总的容量，
					cell[i][j] = max(cell[i-1][j], cur_goods_value + left_value)
				else:
					cell[i][j] = cell[i-1][j]
			print("%d %d %d" % (i, j, cell[i][j]))
'''
	for item in goods.keys():
		processed_goods.append(item)
		print(processed_goods)
		for j in processed_goods:
			for i in range(1, capacity+1):
				if (int(goods[j][0]) <= i and maxValue < int(goods[j][1])):
					maxValue = goods[j][1]
					print("%s %d %d" % (item, i, maxValue))
				if( i == capacity+1):
					left = i - int(goods[j][0])
					left_value = [goods[r][0] for r in goods.keys() if goods[r][0] <= left]
					if (maxValue < left_value + ):
'''					










if __name__ == "__main__":
	print(goods)
	getMaxValueOfPackage()




















