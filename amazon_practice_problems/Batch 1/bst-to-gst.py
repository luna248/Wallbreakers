# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.allGreaterSum = 0
        self.postOrderTraversal(root)
        return root

    def postOrderTraversal(self, root):
        if not root:
            return None
        self.postOrderTraversal(root.right)
        self.allGreaterSum += root.val
        root.val = self.allGreaterSum
        self.postOrderTraversal(root.left)
