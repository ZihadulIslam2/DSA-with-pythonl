# create a node a node that represent a node
# soluthon class for inorder Traversel functon.
# inorder function for recursion .
# print example input.


class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class Solution :

    result = []

    def inorderTraversel(self, root:Optional[TreeNode],->List[]):

        def inorder():
            if root is None:
                return
            
            inorder(root.left)
            result.append(root.left)
            inorder(root.right)

        return result
    

node0 = TreeNode[1]
node1 = root.left[2]
node3 = root.left.right[3]

solution = solution()
print(solution.inorderTraversal())