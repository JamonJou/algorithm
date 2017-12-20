#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： d2_search2.py
# author : zoujiameng@aliyun.com.cn


r'''题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
3,[[1,2,8,9],[3,4,9,12],[4,7,10,13],[6,8,11,15]]
16,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
13,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
16,[[1,2,8,13],[2,4,9,14],[4,7,10,15],[6,8,11,17]]
16,[[1,2,8,9],[3,4,9,12],[4,7,10,13],[13,14,16,17]]'''

def checked(source):
	ilen = len(source[0])
	for i in source[1:]:
		if ilen != len(i): # 每行数据个数相同
			return False

	for i in range(1, len(source)): # 保证是递增的二维数组
		for j in range(1, len(source[0])):
			if int(source[i][j]) < int(source[i][j-1]) or int(source[i][j]) < int(source[i-1][j]) or int(source[i][j]) < int(source[i-1][j-1]):
				#print("found a item not meet", source[i][j])
				return False
	return True

def searchd2array(array, target):
	if checked(array):
		ilen = len(array)
		jlen = len(array[0])
		print(ilen, jlen)
		i,j = 0,jlen-1
		while i < ilen and j >= 0:
			print("cur(%d,%d)" % (i,j), end='')
			if target == int(array[i][j]): # found target
				print(" found ", target)
				return True
			elif target < int(array[i][j]):
				j-=1
				print(" 向左走 ")
			elif target > int(array[i][j]):
				i+=1
				print(" 向下走 " )
		# 如果还是没有找到
		while i < ilen: # 向下走
			if int(array[i][j-1]) == target:
				return True
			print(" 接着向下走 " )
			i+=1
		while j >= 0: # 向左走
			if int(array[i-1][j]) == target:
				return True
			print(" 接着向左走 " )
			j-=1
		return False
	else:
		pass
		#print("The array doesn't meet demand")

def parse2(string):
	n = string.split('[', 1)[1]
	n = n.rsplit(']', 1)[0].strip()
	n = n.split("],[")
	n[0] = n[0].split('[')[1]
	n[-1] = n[-1].rsplit(']')[0]
	arr = []
	for item in n:
		arr.append(item.split(','))
	return arr

if __name__ == "__main__":
	source = str(input())
	target,array = source.split(',', 1)
	array = parse2(array.strip())
	if searchd2array(array, int(target)):
		print("true")
	else:
		print("false")




