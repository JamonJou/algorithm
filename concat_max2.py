#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： concat_max2.py
# author : zoujiameng@aliyun.com.cn

#题目描述
# 设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
# 如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
# 如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。

def checkList(N, Nlist):
	if 1 > N or N > 100:
		print("将要输入的整数太大或者小于1")
		return False

	if N != len(Nlist):
		print("输入项的个数与N不匹配")
		return False

	for i in Nlist:
		if int(i) <= 0 or int(i) >= 1000:
			print("存在数据不在（0，1000）之间")
			return False
	return True

def firstbit(num):
	tmp = int(num)
	if 0 <= tmp < 10:
		return tmp
	else:
		while tmp >= 10:
			tmp = tmp//10
		return tmp

def samePrefix(a, b):# 开头有多少位相同, 返回开头值大的数, a != b
	startSameBit = 0
	tmpa = a
	tmpb = b
	res = 0
	#print("---->", tmpa, "\t", tmpb, "<-------", a, "\t", b)
	while tmpa>0 and  tmpb>0:
		if firstbit(tmpa) == firstbit(tmpb): # 去除共同的前缀???
			tmpa = tmpa//10
			tmpb = tmpb//10
			startSameBit+=1
		else:
			break
	if tmpa == 0 and tmpb != 0:# b的位数多，a的位数少, 比较位数多去掉共同前缀剩下的firstbit与位数少的firstbit
		if firstbit(a) > int(str(b)[startSameBit]):
			res = a
		elif firstbit(a) < int(str(b)[startSameBit]):
			res = b
	elif tmpb == 0 and tmpa != 0:# a的位数多，b的位数少, 比较b的第一位与a的剩余位的首位
		if firstbit(b) > int(str(a)[startSameBit]):
			res = b
		elif firstbit(b) < int(str(a)[startSameBit]):
			res = a
	elif tmpa == 0 and tmpb == 0:# a,b的位数一样
		if tmpa < tmpb:
			res = b
		elif tmpa > tmpb:
			res = a
	else: # 去掉共同的前缀后，剩余的数要比较首位进行比较
		if int(str(a)[startSameBit]) < int(str(b)[startSameBit]):
			res = b
		elif int(str(a)[startSameBit]) > int(str(b)[startSameBit]):
			res = a
	#print("---->", tmpa, "\t", tmpb, "\t", firstbit(res), "\t", res, "startSameBit=", startSameBit)
	return (firstbit(res), res)

'''def diffSame(a, b):
	if a == b: # 两个数相等
		return (firstbit(b), b)
	else: # 两个数不相等
		# 先不比较前面相同的，只看不同处于最开始的大小
		return samePrefix(a, b)
'''
def catN(N, Nlist): # N为int型，Nlist为list
	resList = [] # 存储最终顺序的结果
	if checkList(N, Nlist) and isinstance(Nlist, list):
		for count in range(N):
			maxFirstBit = firstbit(int(Nlist[0])) # 第一个元素，首位最大标记位
			curMax = int(Nlist[0]) # 第一个元素，首位最大标记位的元素
			print("----curMax \t maxFirstBit \t----", end='')
			for i in range(1, len(Nlist)): # 查找当前list中最大开头的值
				item = int(Nlist[i])
				curBit = firstbit(item)
				if maxFirstBit <  curBit:
					maxFirstBit = curBit
					curMax = item
				elif maxFirstBit == curBit: # 相同就比较第2位，依次类推
					if curMax != item: # 不相等, 相等的话就略过
						(maxFirstBit, curMax) = samePrefix(curMax, item) # 当前值与之前保存的数比较
			print("item \tcurMax\t maxFirstBit \t curBit ")
			print(item, "\t", curMax, "\t", maxFirstBit, "\t", curBit)
			print("----curMax \t resList----")
			print(curMax, "\t", resList)
			resList.append(str(curMax))
			Nlist.remove(str(curMax))
			print("resList \t Nlist")
			print(resList, "\t", Nlist)
		return resList
	else:
		pass
		#print(Nlist," len is not ", N)
	return resList

if __name__ == "__main__":
	a = input()
	b = str.split(input())
	ab = catN(int(a), b)
	if ab:
		res = ""
		for i in ab:
			res = res+(i)
		print(res)
