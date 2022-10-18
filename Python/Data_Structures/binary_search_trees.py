#BINARY TREE DATA STRUCTURE AND PRE-ORDER TRAVERSAL, IN-ORDER TRAVERSAL, POST-ORDER TRAVERSAL.
class Node:#We create a class Node. Since we are going to create a binary tree, each node has at most two child nodes.
    def __init__(self, value: int, left=None, right=None):#We accept three parameters: the value of the node, the value of the left child node of the node,
#and the value of the right child node of the node.

    #Defining instance variables. This variables are going to be created automatically when a node object is created. This variables are related to the parameters that we passed
#to the class Node when creating an object.
        self.value = value
        self.left = left
        self.right = right
    
class BinaryTree:#We create a class BinaryTree. So we can have different binary trees that are the result of connecting different nodes in a specific way.
    def __init__(self, root: int):
        self.root = Node(root)#Here we are defining a instance variable called root. This instacnce variable is going to be a node, the root node.
        self.pre_order = []#I will use this list to store Pre-Order Traversal result.
        self.in_order = []#I will use this list to store In-Order Traversal result.
        self.post_order = []#I will use this list to store Post-Order Traversal result.

    def preOrderTraversal(self, root: object):#This function is to traverse the node. In this type of traverse the root node is 
#visited first, then the left subtree and finally the right subtree.
        if root:#We check if the root object exists.
            #print(root.value, end=" --> ")
            self.pre_order.append(root.value)#We append the value of the root to the pre_order instance list variable.
            self.preOrderTraversal(root.left)#We use recursion to call the left node of each node.
            self.preOrderTraversal(root.right)#We use recursion to call the right node of each node. 
        return self.pre_order

    def inOrderTraversal(self, root: object):#This function is to traverse the node. In this type of traverse the left node is vistised, then the 
#current node and then the right node.
        if root:
            self.inOrderTraversal(root.left)
            self.in_order.append(root.value)
            self.inOrderTraversal(root.right)
        return self.in_order

    def postOrderTraversal(self, root: object):#In this type of traversal we visit first the left subtree, then the right subtree, and then the root node.
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            self.post_order.append(root.value)
        return self.post_order

if __name__ == '__main__':
    #Creating the binary tree.
    bt1 = BinaryTree(50)
    bt1.root.left = Node(25)
    bt1.root.right = Node(70)
    bt1.root.left.left = Node(10)
    bt1.root.left.right = Node(27)
    bt1.root.right.left = Node(60)
    bt1.root.right.right = Node(100)
    #The binary tree looks like this:
    #               50
    #            /      \
    #          25        70
    #         /  \      /  \  
    #       10    27   60  100 
    bt2 = BinaryTree(40)
    bt2.root.left = Node(10)
    bt2.root.right = Node(100)
    #The binary tree looks like this:
    #               40
    #             /    \  
    #            10    100
    print(f"\033[1;32;40mPre-Order Traversal:\033[1;33;40m {bt1.preOrderTraversal(bt1.root)}\033[0m")
    print(f"\033[1;32;40mIn-Order Traversal:\033[1;33;40m {bt1.inOrderTraversal(bt1.root)}\033[0m")
    print(f"\033[1;32;40mPost-Order Traversal:\033[1;33;40m {bt1.postOrderTraversal(bt1.root)}\033[0m")
    print(f"\033[1;32;40mPre-Order Traversal:\033[1;33;40m {bt2.preOrderTraversal(bt2.root)}\033[0m")
    print(f"\033[1;32;40mIn-Order Traversal:\033[1;33;40m {bt2.inOrderTraversal(bt2.root)}\033[0m")
    print(f"\033[1;32;40mPost-Order Traversal:\033[1;33;40m {bt2.postOrderTraversal(bt2.root)}\033[0m")
    
