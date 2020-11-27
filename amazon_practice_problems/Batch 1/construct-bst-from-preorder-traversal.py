# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        first = preorder[0]
        root = TreeNode(first)

        lowerThanRoot, greaterThanRoot = [], []
        for i in range(1, len(preorder)):
            if preorder[i] < first:
                lowerThanRoot.append(preorder[i])
            else:
                greaterThanRoot.append(preorder[i])

        root.left = self.bstFromPreorder(lowerThanRoot)
        root.right = self.bstFromPreorder(greaterThanRoot)

        return root
