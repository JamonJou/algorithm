#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# fileName ： tree_high.py
# author : zoujiameng@aliyun.com.cn

'''时间限制：1秒 空间限制：32768K

题目描述
	现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度

输入描述:
	输入的第一行表示节点的个数n（1 ≤ n ≤ 1000，节点的编号为0到n-1）组成，下面是n-1行，每行有两个整数，第一个数表示父节点的编号，第二个数表示子节点的编号
输出描述:

输出树的高度，为一个整数
	示例1
	输入

	5
	0 1 # root = BinaryTree(0) root.insertLeft(BinaryTree(1))
	0 2 # root.getRootVal() == 0 root.insertRight(BinaryTree(2))
	1 3 # root.leftChild.getRootVal() == 1 root.leftChild.insertLeft(BinaryTree(3))
	1 4 # root.leftChild.getRootVal() == 1 root.leftChild.insertRight(BinaryTree(4))

	输出

	3'''
tree = [ '0', # root
	['1', # left child
		['3'],['4'] 
	],
	['2', # right child
		[''],['']
	]
]

tree[0] #root 
tree[1] #left sub-tree
tree[2] #right sub-tree

class Node():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.leftChild = left
		self.rightChild = right

	def getRootVal(self):
		return self.value

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.value = obj

def depth(atree):
	if atree == None:
		return 0
	nleft = depth(atree.leftChild)
	nright = depth(atree.rightChild)
	if nleft > nright:
		return nleft+1
	else:
		return nright+1

def printTreeByFirstOrder(root): # First Order trace tree
	if root != None:
		print(root.getRootVal(), end='\t')
		if root.getLeftChild():
			printTreeByFirstOrder(root.getLeftChild())
		if root.getRightChild():
			printTreeByFirstOrder(root.getRightChild())

def getRootNode(tree, curValue):
	#print("type(tree)", type(tree), "tree.getRootVal = ", tree.getRootVal(), "curValue = ", curValue)
	if tree.getRootVal() == curValue:
		#print(" found ", curValue)
		return tree
	elif tree.leftChild:
		#print("search left tree...", end='')
		return getRootNode(tree.leftChild, curValue) # search left tree
	elif tree.rightChild:
		#print("search right tree...", end='')
		return getRootNode(tree.rightChild, curValue) # search right tree

def initTree(root, parentValue, childValue):
	if root.getRootVal() == None:
		root = Node(parentValue)
		root.leftChild = Node(childValue)
	else:
		tmp = getRootNode(root, parentValue) # 获取当前插入点的子树根节点
		#print("type(tree)", type(tmp), "tree.getRootVal = ", tmp.getRootVal(), end='\t')
		if tmp != None:
			node = Node(childValue)
			if tmp.getRootVal() != None:
				if tmp.leftChild == None:
					tmp.leftChild = node
					#print("tree.leftChild = ", tmp.leftChild.getRootVal())
				elif tmp.rightChild == None:
					tmp.rightChild = node
					#print("tree.rightChild = ", tmp.rightChild.getRootVal())
				else:
					pass
	return root # return root

if __name__ == "__main__":
	N = int(input())
	root = Node(None)
	i = 1
	while i < N: # init tree
		source  = str.split(input())
		rootValue = source[0]
		childValue = source[1]
#		print("source = ", source, "rootValue =  ", rootValue, " childValue = ", childValue)
		root = initTree(root, rootValue, childValue)
		i += 1
#		print("printTreeByFirstOrder", "root", end='\t')
#		printTreeByFirstOrder(root)
#		print()

	print(depth(root))
	printTreeByFirstOrder(root)


























