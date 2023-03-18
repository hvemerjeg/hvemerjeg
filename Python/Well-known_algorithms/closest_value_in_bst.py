#THIS CODE IS THE SOLUTION TO A PROBLEM CALLED "FINDING THE CLOSEST VALUE IN BST". 
#We are given a binary search tree and a target value, and we need to find the closest value to the target value in the binary search tree.
#A binary search tree is a type of binary tree(a binary tree is a type of tree where each node has at most two child nodes.) where the nodes with value
#higher or equal to its parent node are placed on the right side of the parent node and the values that are minor than its parent node are
#placed on the left side of the parent node.
#For example:
#           50
#         /    \
#       40      52
#      /  \    /  \
#    20   45  51  53 
#      \
#      30
#So to solve this problem we are going to construct a binary search tree.
#And the function to solve the problem could be placed inside the class of our binary search tree as a method, or outside the binary search tree as a regular function.

#Constructing a binary search tree.
class Node: #We begin constructing the class Node. As you can see, each node has a value and also each node has at most two values associated with it.
#Those two values are the child nodes.
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree: #Here we are constructing the class BinaryTree. A binary tree is treated as an object that at the same time contains nodes(that are also objects).
    def __init__(self, root: int):
        self.root = Node(root)
        self.closest = float('inf') #This instance variable will be useful to store the closest value, this is the result that the problem is requesting.

    def findClosestValue(self, tree: object, target: int, closest=float('inf')): #This is the method that we are going to use to solve the problem.
        if tree: #Here we are checking if the tree is not none. So if the tree is not none do the following.
            if abs(target - tree.value) < abs(target - closest): #We need to think that our target value is kind of a limit, and we want to get as close
#as possible to this limit from the right or from the left(think about a number line) as follows:
#          -------------------------------
#                   -->   |   <--
#                       target
#That is the reason why we are using the absolute value, because it does not matter if we are approaching the target value from a lower value or a higher value.
#Imagine that our target value is the number 2. If we have a node with a value of 3 we subtract 3 from 2 = -1, but we do not care about the negative sign.
#We know that we are just one step away from the target and that is what matters in this problem.
                self.closest = tree.value
            if tree.value < target: #If the value of the current node is higher than the target, making use of the fact that all the higher values of a node
#are placed to the right side and all the lower values are placed to left side of the node, we can use recursion to travel depending of
#the result of comparing the target and the value of the current node.
                self.findClosestValue(tree.right, target, self.closest)
            elif tree.value > target:
                self.findClosestValue(tree.left, target, self.closest)
            else: #If the value of the current node is equal to the target we return the value of the instance variable self.closest.
                return self.closest
        return self.closest

if __name__ == '__main__':
    #Here we are creating the binary search tree.
    bt1 = BinaryTree(50)
    bt1.root.left = Node(40)
    bt1.root.right = Node(52)
    bt1.root.left.left = Node(20)
    bt1.root.left.right = Node(45)
    bt1.root.right.left = Node(51)
    bt1.root.right.right = Node(53)
    bt1.root.left.left.right = Node(30)
    print(bt1.findClosestValue(bt1.root, 31))
