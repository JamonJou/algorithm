
class BinaryTree():
	def __init__(self, rootNode):
		self.key = rootNode
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = newNode
		else:
			node = BinaryTree(newNode)
			node.leftChild = self.leftChild
			self.leftChild = node

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = newNode
		else:
			node = BinaryTree(newNode)
			node.rightChild = self.rightChild
			self.rightChild = node

	def delLeft(self, Node):
		if Node != None and Node.leftChild != None:
			tmp = Node.leftChild
			Node.leftChild = None
			return tmp

	def delRight(self, Node):
		if Node != None and Node.rightChild != None:
			tmp = Node.rightChild
			Node.rightChild = None
			return tmp

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key
