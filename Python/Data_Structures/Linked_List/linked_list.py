#THIS IS AN IMPLEMENTATION OF A SINGLY LINKED LIST
#I will implement some basic linked list algorithms

class Node:
	def __init__(self, value, nxt=None):
		self.value = value
		self.next = nxt

class LinkedList:
	def __init__(self, head):
		self.head = Node(head)

	def getHead(self):
		return self.head.value

#Traversing through the linked list
def linkedListTraversal(head: object):
	#I will implement this traversal with recursion
	if head:
		print(f"\033[1;36;40m{head.value}\033[0m", end="\033[1;36;40m --> \033[0m")
		linkedListTraversal(head.next)	
#Returning the sum of all the values present on the linked list
def sumLinkedList(head: object):
	#Recursion
	suma = 0
	if head:
		suma += head.value
		suma += sumLinkedList(head.next)
	return suma	

#Find node
def findNode(head: object, node):
	if head:
		if head.value == node:
			return True
		if findNode(head.next, node) == True:
			return True
	return False

#Find node at specific index
def getNodeValue(head: object, indx: int):
	#I will implement this algorithm without recursion
	current = head
	while current:
		if indx == 0:
			return current.value
		current = current.next
		indx -= 1
	return False

if __name__ == '__main__':
	l1 = LinkedList(100)
	l1.head.next = Node(50)
	l1.head.next.next = Node(101)
	l1.head.next.next.next = Node(3)
	l1.head.next.next.next.next = Node(5050)
	print(f"\033[1;36;40mLinked list traversal: \033[0m")
	linkedListTraversal(l1.head)
	print()
	print()
	print(f"\033[1;36;40mLinked list sum: \033[0m")
	print(f"\033[1;36;40m{sumLinkedList(l1.head)}\033[0m")
	print()
	print(f"\033[1;36;40mFind node: \033[0m")
	print(f"\033[1;36;40m{findNode(l1.head, 5050)}\033[0m")
	print()
	print(f"\033[1;36;40mGet node value: \033[0m")
	print(f"\033[1;36;40m{getNodeValue(l1.head, 2)}\033[0m")
