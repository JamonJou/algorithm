#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： robot_path.py
# author : zoujiameng@aliyun.com.cn

# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
class Robot:
	def movingCount(self, threshold, rows, cols):
		#"产生 0 矩阵 "
		board=[[0 for i in range(cols)] for j in range(rows)]
		global acc
		acc = 0
		#"下标之和,若大于threshold则TRUE,否则Folse"
		def block(r,c):
		    s=sum(map(int,str(r)+str(c)))
		    return s>threshold
		def traverse(r,c):
			global acc
			if not (0<=r<rows and 0<=c<cols):   # 超出角标范围挑出
				return
			if board[r][c] != 0:    # 不等于0 跳出
				return
			if board[r][c] == -1 or block(r,c):
				board[r][c]=-1    #超出门限的点记录-1
				return

			board[r][c]=1 #符合规定的点记录1，并计数加一
			acc+=1
			traverse(r+1,c)
			traverse(r-1,c)
			traverse(r,c+1)
			traverse(r,c-1)
		traverse(0,0)
		return acc

o = Robot()
print(o.movingCount(1 , 3 ,3))
