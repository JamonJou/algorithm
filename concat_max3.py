#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： concat_max.py
# author : zoujiameng@aliyun.com.cn

#题目描述
# 设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
# 如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
# 如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
# 采用桶: dict [0-9] 每个value都是一个list
def checkList(Nlist): # 检查list中的每一个元素是否是0-1000
	for i in Nlist:
		if int(i) <= 0 or int(i) >= 1000:
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

def samePrefixBig(a, b):# 比较两个不同的数a和b，不考虑开头相同的位, 返回开头值大的数, a != b
	tmpa = str(a)
	tmpb = str(b)
	res = b

	startSameBit = 0
	alen = len(tmpa)
	blen = len(tmpb)
	while alen>0 and blen>0:
		if tmpa[0] == tmpb[0]: # 去除共同的前缀
			tmpa = tmpa[1:]
			tmpb = tmpb[1:]
			alen -= 1
			blen -= 1
			startSameBit += 1	
		else:
			break
	if alen == 0 and blen != 0:# b的位数多，a的位数少, 且a为b的前缀
		while blen>0 and firstbit(a) == int(tmpb[0]):
			tmpb = tmpb[1:]
			blen -= 1
			#print("A---> ")
	#if blen>0:
		if firstbit(a) > int(tmpb[0]):
			res = a
		elif firstbit(a) < int(tmpb[0]):
			res = b
	#else:
		#res = a
		#print("A---> %d位数少于%d,剩余长度为(%d, %d), %d, %d" % (a, b, alen, blen, firstbit(a), int(tmpb[0])))
	elif blen == 0 and alen != 0:# a的位数多，b的位数少, 且b为a的前缀
		while alen>0 and firstbit(b) == int(tmpa[0]):
			tmpa = tmpa[1:]
			alen -= 1
			#print("B---> ")
	#if alen>0:
		if firstbit(b) > int(tmpa[0]):
			res = b
		elif firstbit(b) < int(tmpa[0]):
			res = a
	#else:
		#res = b
		#print("B---> %d位数多于%d,剩余长度为(%d, %d), %d, %d" % (a, b, alen, blen, firstbit(b), int(tmpa[0])))
	elif alen == 0 and blen == 0:# a,b的位数一样，且只有最后一位不同
		if int(tmpa) < int(tmpb):
			res = b
		elif int(tmpa) > int(tmpb):
			res = a
	else: # 去掉共同的前缀后，剩余的数要比较首位进行比较
		if int(tmpa[0]) < int(tmpb[0]):
			res = b
		elif int(tmpa[0]) > int(tmpb[0]):
			res = a
	#print("比较 %d 和 %d, (%s, %s)相同前缀位数为%d,规则大者为 %d" % (a, b, tmpa, tmpb, startSameBit, res))
	return res

def sortListByFirstBit(alist):
	if len(alist) >= 2:
		resList = []
		for count in range(len(alist)):
			curMax = alist[0]
			for item in alist[1:]: # 查找当前list中最大开头的值
				if curMax != item:
					curMax = samePrefixBig(item, curMax)
			resList.append(curMax)
			alist.remove(curMax)
		#print(resList)
		return resList
	else:
		return alist	

def sortFirstBit(N, Nlist):
	tuple09 = ('0','1','2','3','4','5','6','7','8','9')
	abdict = {}
	resList = []
	if checkList(Nlist) and N == len(Nlist):
		for i in Nlist: # 构造dict
			tmp = int(i)
			index = tuple09[firstbit(tmp)]
			if index in abdict.keys(): #已经有相同的首位
				abdict[index].append(tmp)
			else: #没有相同的首位
				alist = []
				alist.append(tmp)
				abdict[index] = alist
		for key in sorted(abdict.keys(), reverse=True):
			#print(type(abdict[key]), "\t", abdict[key])
			valueList = sortListByFirstBit(abdict[key])
			# 对valueList进行排序，然后存放到结果集resList中
			resList.append(valueList)
			#print(key, valueList)
	else:
		pass
		#print("input numbers happened errors")
	return resList

if __name__ == "__main__":
	a = input()
	b = str.split(input())
	ab = sortFirstBit(int(a), list(b))
	if ab:
		res = ""
		for item in ab:
			for cur in item:
				res=res+str(cur)
		print(res)
