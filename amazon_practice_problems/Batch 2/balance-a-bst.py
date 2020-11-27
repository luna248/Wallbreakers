# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createNewTree(self, listOfNodes, start, end):
        if start > end:
            return

        mid = (start + end) // 2
        root = TreeNode(listOfNodes[mid])
        root.left = self.createNewTree(listOfNodes, start, mid-1)
        root.right = self.createNewTree(listOfNodes, mid+1, end)
        return root

    def inOrderList(self, root, listOfNodes):
        if root is  None:
            return

        if root:
            self.inOrderList(root.left, listOfNodes)
            listOfNodes.append(root.val)
            self.inOrderList(root.right, listOfNodes)

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        listOfNodes = []
        self.inOrderList(root, listOfNodes)
        return self.createNewTree(listOfNodes, 0, len(listOfNodes)-1)
