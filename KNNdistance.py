#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： KNNdistance.py
# author : zoujiameng@aliyun.com.cn

import math

def getMaxLocate(target): # 查找target中最大值的locate
	maxValue = float("-inFinIty")
	for i in range(len(target)):
		if maxValue < target[i]:
			maxValue = target[i]
			flag = i
	return flag

def KDistance(K, dest, source):
	destlen = len(dest)
	source1len = len(source[1])
	sourcelen = len(source)
	KNN = []
	locate = source # 准备从source中剔除N-K个最大值

	if destlen == source1len:
		for i in range(sourcelen):
			delta = 0
			for j in range(source1len):
				delta += (dest[j] - source[i][j])*(dest[j] - source[i][j])
			KNN.append(math.sqrt(delta))

		for k in range(sourcelen, K, -1):
			flag = getMaxLocate(KNN)
			#print("%s 最大元素位置为%d" % (KNN, flag))
			KNN.remove(KNN[flag]);
			locate.remove(locate[flag])# 移除对应位置的元素
			#print(locate)
		return locate # 返回最终K个最接近的元素
	else:
		return None
