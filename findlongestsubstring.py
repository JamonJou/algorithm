#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 对于最长公共子串问题,答案为网格中最大的数字——它可能并不位于最后的单元格中

def findlongestsubstring(source, dest): # 输入值(内循环)， 要比较的目标(外循环)
	inLen = len(source)
	outLen = len(dest)

	start = -1
	end = -1
	maxlen = 0

	cell = [ [0 for j in range(inLen+1)] for i in range(outLen+1)]

	for i in range(1, outLen+1):
		for j in range(1, inLen+1):
			if dest[i-1] == source[j-1]: # 字母相同
				#start = j - 1
				#end = start + 1
				cell[i][j] = cell[i-1][j-1] + 1
				if maxlen < cell[i][j]: # 找到新的子串
					if cell[i][j] == 1:# or cell[i][j] == maxlen:
						start = j - 1
						end = start + 1
					else:
						end+=1
					maxlen = cell[i][j]
			else: # 字母不同
				cell[i][j] = 0
		print("maxLen = %d , %d %d" % (maxlen, start, end))
	print(">>>>>>maxLen = %d , %d %d" % (maxlen, start, end))

	for i in range(1, outLen+1):
		print(cell[i])
	longest = -1
	flag = -1
	for i in range(1, outLen+1):
		for j in range(1, inLen+1):
			if longest < cell[i][j]:
				longest = cell[i][j]
				flag = j
	print("max = %d, end = %d" % (longest, flag))
	print("The Longest sub string of \"%s\" and \"%s\" is \"%s\"" % (source, dest, dest[flag-longest:flag]))
	return cell

def getlongestsubstring(cell):
	longest = 0
	for i in range(1, outLen+1):
		for j in range(1, inLen+1):
			if longest < cell[i-1][j-1]:
				longest = cell[i-1][j-1]
				flag = j - 1
	print()
if __name__ == "__main__":
	#findlongestsubstring("hisha", "fish")
	#print()
	findlongestsubstring("hish", "vista")
	#print()
	#findlongestsubstring("hish", "hash")
