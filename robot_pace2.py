#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： robot_path.py
# author : zoujiameng@aliyun.com.cn

# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
class Robot:
# 共用接口,判断是否超过K
	def getDigitSum(self, num):
		sumD = 0
		while(num>0):
			sumD+=num%10
			num/=10
		return int(sumD)

	def PD_K(self, rows, cols, K):
		sumK = self.getDigitSum(rows) + self.getDigitSum(cols)
		if sumK > K:
			return False
		else:
			return True

	def PD_K1(self, i, j, k):
		"确定该位置是否可以走,将复杂约束条件设定"
		index = map(str,[i,j])
		sum_ij = 0
		for x in index:
			for y in x:
				sum_ij += int(y)
		if sum_ij <= k:
			return True
		else:
			return False

# 共用接口,打印遍历的visited二维list
	def printMatrix(self, matrix, r, c):
		print("cur location(", r, ",", c, ")")
		for x in matrix:
			for y in x: 
				print(y, end=' ')
			print()

 #回溯法
	def hasPath(self, threshold, rows, cols):
		visited = [ [0 for j in range(cols)] for i in range(rows) ]
		count = 0
		startx = 0
		starty = 0
		#print(threshold, rows, cols, visited)
		visited = self.findPath(threshold, rows, cols, visited, startx, starty, -1, -1)
		for x in visited:
			for y in x:
				if( y == 1):
					count+=1
		print(visited)
		return count

	def findPath(self, threshold, rows, cols, visited, curx, cury, prex, prey):
		if 0 <= curx < rows and 0 <= cury < cols and self.PD_K1(curx, cury, threshold) and visited[curx][cury] != 1: # 判断当前点是否满足条件
			visited[curx][cury] = 1
		self.printMatrix(visited, curx, cury)
		prex = curx
		prey = cury
		if cury+1 < cols and self.PD_K1(curx, cury+1, threshold) and visited[curx][cury+1] != 1: # east
			visited[curx][cury+1] = 1
			return self.findPath(threshold, rows, cols, visited, curx, cury+1, prex, prey)
		elif cury-1 >= 0 and self.PD_K1(curx, cury-1, threshold) and visited[curx][cury-1] != 1: # west
			visited[curx][cury-1] = 1
			return self.findPath(threshold, rows, cols, visited, curx, cury-1, prex, prey)
		elif curx+1 < rows and self.PD_K1(curx+1, cury, threshold) and visited[curx+1][cury] != 1: # sourth
			visited[curx+1][cury] = 1
			return self.findPath(threshold, rows, cols, visited, curx+1, cury, prex, prey)
		elif 0 <= curx-1  and self.PD_K1(curx-1, cury, threshold) and visited[curx-1][cury] != 1: # north
			visited[curx-1][cury] = 1
			return self.findPath(threshold, rows, cols, visited, curx-1, cury, prex, prey)
		else: # 返回上一层,此处有问题
			return visited#self.findPath(threshold, rows, cols, visited, curx, cury, prex, prey)
 #回溯法2
	def movingCount(self, threshold, rows, cols):
		visited = [ [0 for j in range(cols)] for i in range(rows) ]
		print(visited)
		count = self.movingCountCore(threshold, rows, cols, 0, 0, visited);
		print(visited)
		return count

	def movingCountCore(self, threshold, rows, cols, row, col, visited):
		cc = 0
		if(self.check(threshold, rows, cols, row, col, visited)):  
			visited[row][col] = 1
			cc = 1 + self.movingCountCore(threshold, rows, cols, row+1, col,visited) + self.movingCountCore(threshold, rows, cols, row, col+1, visited) + self.movingCountCore(threshold, rows, cols, row-1, col, visited) + self.movingCountCore(threshold, rows, cols, row, col-1, visited)
		return cc

	def check(self, threshold, rows, cols, row, col, visited):
		if( 0 <= row < rows and 0 <= col < cols and (self.getDigitSum(row)+self.getDigitSum(col)) <= threshold and visited[row][col] != 1): 
			return True;
		return False 

# 暴力法，直接用当前坐标和K比较
	def force(self, rows, cols, k):
		count = 0
		for i in range(rows):
			for j in range(cols):
				if self.PD_K(i, j, k):
					count+=1
		return count
# 暴力法2, 用递归法来做
	def block(self, r, c, k): 
		s = sum(map(int, str(r)+str(c)))
		return s>k
	def con_visited(self, rows, cols):
		visited = [ [0 for j in range(cols)] for i in range(rows) ]
		return visited
	def traval(self, r, c, rows, cols, k, visited):
		if not (0<=r<rows and 0<=c<cols):
			return
		if visited[r][c] != 0 or self.block(r, c, k):
			visited[r][c] = -1
			return
		visited[r][c] = 1
		global acc
		acc+=1
		self.traval(r+1, c, rows, cols, k, visited)
		self.traval(r, c+1, rows, cols, k, visited)
		self.traval(r-1, c, rows, cols, k, visited)
		self.traval(r, c-1, rows, cols, k, visited)
		return acc

if __name__ == "__main__":
	# 调用测试
	m = 3
	n = 3
	k = 1
	o = Robot()
	print(o.hasPath(k, m, n))
	print(o.force(m,n,k))
	global acc
	acc = 0
	print(o.traval(0, 0, m, n, k, o.con_visited(m,n)))
	print(o.movingCount(k, m, n))
