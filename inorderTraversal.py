

"""
- TreeNode Class: The TreeNode class represents a node in a binary tree. Each node has a value (val), a left child (left), and a right child (right).
- Solution Class: The Solution class contains the method inorderTraversal, which takes the root of a binary tree as an argument and returns a list of values representing the inorder traversal of the tree.



- Inorder Traversal: Inorder traversal of a binary tree visits nodes in the following order:

    Visit the left subtree
    Visit the current node
    Visit the right subtree

- Recursive Function: The inorder function is defined within inorderTraversal to perform the actual traversal:

    If the current node (root) is None, it returns immediately (base case).
    It recursively calls itself on the left child of the current node.
    It appends the value of the current node to the result list (res).
    It then recursively calls itself on the right child of the current node.

- Return Statement: After the recursive traversal is complete, the method returns the list res, which contains the values of the nodes in inorder sequence.
"""


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

# Example binary tree:
#     1
#      \
#       2
#      /
#     3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2]