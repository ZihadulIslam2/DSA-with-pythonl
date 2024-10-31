"""
Alright! Let's break this down simply, like a story:

Imagine you have a magical tree. Each part of the tree is called a "node," and every node has a number (called `val`) and might have two little branches: one going to the left (called `left`) and one going to the right (called `right`).

Now, you have a mission: visit each part of the tree, but there's a special order you need to follow:

1. **Look at the number on the current node.**
2. **Go to the left branch first.**
3. **Then go to the right branch.**

This order is called **preorder traversal** because we check the node first, then go to the left, and then to the right.

The code works like this:

1. We start with an empty list called `res`, where we’ll store the numbers in the order we visit them.
2. We create a helper function called `preorder` to visit the nodes.
3. The `preorder` function:
   - **If the node is empty (doesn’t exist)**, it just stops and returns.
   - **If the node exists**, it adds its number to `res`.
   - Then, it calls itself to visit the left node (going down the left branch).
   - After finishing with the left side, it calls itself to visit the right node.

Finally, after visiting all nodes in this order, `res` has the numbers in the special preorder way. """


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def preordr(root):
            if not root:
                return
            res.append(root.val)
            preordr(root.left)
            preordr(root.right)

        preordr(root)   
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
print(solution.preorderTraversal(root))  # Output: [1, 3, 2]