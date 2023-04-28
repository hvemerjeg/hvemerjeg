#!/usr/bin/python3

#Colors
green = "\033[1;32;40m"
reset_color = "\033[0m"

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def insertNode(self, value):
		#No recursion
		queue = [self]
		while len(queue):
			current_node = queue.pop(0)
			if value < current_node.value:
				if current_node.left is None:
					current_node.left = Node(value)
				else:
					queue.append(current_node.left)
			else:
				if current_node.right is None:
					current_node.right = Node(value)
				else:
					queue.append(current_node.right)
	
	def findClosest(self, target):
		result = float("inf")
		queue = [self]
		while len(queue): #And probable other thing
			current_node = queue.pop(0)
			if abs(target - current_node.value) < abs(target - result):
				result = current_node.value
			if target < current_node.value:
				if current_node.left is None:
					return result
				else:
					queue.append(current_node.left)
			elif target > current_node.value:
				if current_node.right is None:
					return result
				else:
					queue.append(current_node.right)
			else:
				return current_node.value

def createBST(nodes: list):
	bst = Node(nodes[0])
	for i in range(1, len(nodes)):
		bst.insertNode(nodes[i])
	return bst

def preOrderTraversal(tree: object):
	if tree:
		print(tree.value, end=" --> ")
		preOrderTraversal(tree.left)
		preOrderTraversal(tree.right)

def inOrderTraversal(tree: object):
	if tree:
		inOrderTraversal(tree.left)
		print(tree.value, end=" --> ")
		inOrderTraversal(tree.right)

def postOrderTraversal(tree: object):
	if tree:
		postOrderTraversal(tree.left)
		postOrderTraversal(tree.right)
		print(tree.value, end=" --> ")

if __name__ == '__main__':
	bst1 = createBST([10, 5, 15, 2, 5, 13, 22, 1, 14])
	print(bst1.findClosest(12))
#	print(f"{green}Pre-order traversal: {reset_color}", end="")
#	preOrderTraversal(bst1)
#	print()
#	print(f"{green}In-order traversal: {reset_color}", end="")
#	inOrderTraversal(bst1)
#	print()
#	print(f"{green}Post-order taversal: {reset_color}", end="")
#	postOrderTraversal(bst1)
