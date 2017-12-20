#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： concat_max.py
# author : zoujiameng@aliyun.com.cn

#题目描述
# 设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
# 如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
# 如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
# 采用dict来存储有个弊端，输入数据不能出现重复的数据，所以这种方式要淘汰
# 采用桶: dict [0-9] 每个value都是一个list
def checkList(Nlist):
	for i in Nlist:
		if int(i) <= 0 or int(i) >= 1000:
			return False
	return True

def sortFirstBit(N, Nlist):
	abdict = {}
	if checkList(Nlist) and N == len(Nlist):
		for i in Nlist:
			tmp = int(i)
			if 0 < tmp < 10:
				abdict[tmp*100] = tmp
			elif 10 <= tmp < 100:
				abdict[tmp*10] = tmp
			else:
				abdict[tmp] = tmp
	else:
		print("input numbers happened errors")
	return abdict

if __name__ == "__main__":
	a = input()
	b = str.split(input())
	ab = sortFirstBit(int(a), list(b))
	if ab:
		res = ""
		for key in sorted(ab.keys(), reverse=True):
			value = ab[key]
			res = res+str(value)
		print(res)
		print(len(res))
		res1 = ""
		for y in list(b):
			res1 = res1+y
		print(res1)
		print(len(res1))
