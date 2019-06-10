#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： d2_search.py
# author : zoujiameng@aliyun.com.cn



r'''题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]'''

def isAddList(alist): # 检查是否是递增序列
	start = alist[0]
	for item in alist[1:]:
		if start > item:
			return False
		start = item
	return True

def checked(source):
	#print("checking........", end='')
	ilen = len(source[0])
	#print("len of source is ", ilen)
	for i in source[1:]:
		#print("current item len is ", len(i))
		if ilen != len(i): # 每行数据个数相同
			return False

	for i in range(1, len(source)): # 保证是递增的二维数组
		for j in range(1, len(source[0])):
			if int(source[i][j]) < int(source[i][j-1]) or int(source[i][j]) < int(source[i-1][j]) or int(source[i][j]) < int(source[i-1][j-1]):
				#print("found a item not meet", source[i][j])
				return False
	#print("check out. ok....")
	return True

def searchd2array(array, target):
	if checked(array):
		#print("The array is satisified requirements")
		ilen = len(array)
		jlen = len(array[0])
		print(ilen, jlen)
		i,j = 0,0
		while i < ilen and j < jlen:
			if int(array[i][j]) == target: # found target
				print("found ", target)
				return True
			elif int(array[i][j]) > target: # 
				print("not found ", target)
				return False
			elif int(array[i][j]) < target: # 
				if target >= array[i+1][j+1]: # 比右下角的数还要大
					i+=1
					j+=1
					print("向右下走 " )
				elif target < array[i+1][j+1]: # 比右下角的数小
					if int(array[i][j+1]) <= int(array[i+1][j]): # 如果右边的数小于等于下边的数
						if target >= int(array[i][j+1]):
							if target < int(array[i+1][j]):
								print("1向右走 " )
								j+=1
							else:
								print("1向下走 " )
								i+=1
						elif target <= int(array[i][j+1]):
							print("1向下走 " )
							i+=1
						elif target < int(array[i+1][j]):
							print()
							
						else:
							print("not found ", target)
					elif int(array[i][j+1]) > int(array[i+1][j]): # 如果右边的数大于下边的数
						if target <= int(array[i+1][j]):
							print("2向下走 " )
							i+=1
						elif target > int(array[i+1][j]):
							print("2向右走 " )
							j+=1
			print("cur(%d,%d)=%d" % (i,j,array[i][j]))
		# 如果还是没有找到
		while i < ilen: # 向下走
			if int(array[i][j]) == target:
				return True
			print("接着向下走 " )
			i+=1
		while j < jlen: # 向右走
			if int(array[i][j]) == target:
				return True
			print("接着向右走 " )
			j+=1
		return False
	else:
		pass
		#print("The array doesn't meet demand")
def parse(string):
	arr = []
	for c in string:
		print("parse ", c, " ...")
		if c == '[':
			tmp = []
		elif c == ']':
			arr.append(tmp)
		elif c == ',':
			pass
		else:
			arr.append(c)
	return arr

def parse2(string):
	n = string.split('[', 1)[1]
	n = n.rsplit(']', 1)[0].strip()
	n = n.split("],[")
	n[0] = n[0].split('[')[1]
	n[-1] = n[-1].rsplit(']')[0]
	arr = []
	for item in n:
		arr.append(item.split(','))
	#print(arr)
	return arr

if __name__ == "__main__":
	source = str(input())
	target,array = source.split(',', 1)
	array = parse2(array.strip())
	print(target, array)
	if searchd2array(array, int(target)):
		print("true")
	else:
		print("false")




