#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 最长公共子序列
# fish fosh >>> fsh
def findlongestsubstring(source, dest): # 输入值， 要比较的值
	inLen = len(source)
	outLen = len(dest)

	target = []
	cell = [ [0 for j in range(inLen+1)] for i in range(outLen+1)]

	for i in range(1, outLen+1):
		for j in range(1, inLen+1):
			if dest[i-1] == source[j-1]:
				cell[i][j] = cell[i-1][j-1] + 1
				target.append(dest[i-1])
			else:
				cell[i][j] = max(cell[i-1][j], cell[i][j-1])
	for i in range(1, outLen+1):
		for j in range(1, inLen+1):
			print(cell[i][j], end=', ')
		print()
	print("The Longest sub sequence of \"%s\" and \"%s\" is %s" % (source, dest, target))

if __name__ == "__main__":
	findlongestsubstring("fish", "fosh")

