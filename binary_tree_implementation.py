class binaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def prinTree(root):
    if root == None:
        return

    print(root.data,end=": ")
    if root.left != None:
        print("L",root.left.data,end=": ")
    if root.right != None:
        print("R",root.right.data,end=": ")
    print()

    prinTree(root.left)
    prinTree(root.right)

"""
btn1 = binaryTreeNode(1)
btn2 = binaryTreeNode(2)
bth3 = binaryTreeNode(3)

btn1.left=btn2
btn1.right=bth3

prinTree(btn1)
"""

# big tst case:

# Define nodes
root = binaryTreeNode(1)
node2 = binaryTreeNode(2)
node3 = binaryTreeNode(3)
node4 = binaryTreeNode(4)
node5 = binaryTreeNode(5)
node6 = binaryTreeNode(6)
node7 = binaryTreeNode(7)
node8 = binaryTreeNode(8)
node9 = binaryTreeNode(9)

# Construct the tree
root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left = node8
node5.right = node9

# Print the tree
prinTree(root)
