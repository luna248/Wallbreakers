# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        total=0
        if(root.val%2==0):
            if root.right:
                if root.right.left:
                    total+= root.right.left.val
                if root.right.right:
                    total+= root.right.right.val
            if root.left:
                if root.left.left:
                    total+= root.left.left.val
                if root.left.right:
                    total+= root.left.right.val


        total += self.sumEvenGrandparent(root.right)
        total += self.sumEvenGrandparent(root.left)

        return total
