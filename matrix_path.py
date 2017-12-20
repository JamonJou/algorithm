#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： matrix_path.py
# author : zoujiameng@aliyun.com.cn

class MatrixPath():
	def hasPath(self, matrix, rows, cols, path):
		print("rows = %d, cols = %d" % (rows, cols))
		for i in range(rows):
			for j in range(cols):
				if matrix[i*cols+j] == path[0]: # 找到起始点
					if self.findPath(list(matrix), rows, cols, path[1:], i, j):
						return True
		return False
	def findPath(self, matrix, rows, cols, path, x, y):
		if not path: # 找完了？
			return True
		# 将当前位置标记为已走过
		matrix[x*rows+y]='*'
		if y+1 < cols and matrix[x*cols+y+1] == path[0]: # 比较东边
			return self.findPath(matrix, rows, cols, path[1:], x, y+1)
		elif x-1 >= 0 and matrix[(x-1)*cols+y] == path[0]: # 比较北边
			return self.findPath(matrix, rows, cols, path[1:], x-1, y)
		elif y-1 >= 0 and matrix[x*cols+y-1] == path[0]: # 比较西边
			return self.findPath(matrix, rows, cols, path[1:], x, y-1)
		elif x+1 < rows and matrix[(x+1)*cols+y] == path[0]: # 比较南边
			return self.findPath(matrix, rows, cols, path[1:], x+1, y)
		else:
			return False

if __name__ == "__main__":
	# 调用测试
	_matrix = 'abcesfcsadee'
#	_path = 'see'
	_path = 'bcced'
	path = MatrixPath()
	print(path.hasPath(_matrix, 3, 4, _path))
