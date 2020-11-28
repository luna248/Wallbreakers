# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest=[]

        #deques are really helpful for BFS solutions
        queue = deque([(root, None)])

        while queue:
            currNode, nodeParent = queue.popleft()

            #check if node is good to be added to the forest
            if (not nodeParent or nodeParent.val in to_delete) and currNode.val not in to_delete:
                forest.append(currNode)

            #If in to_delete, remove child associations
            if currNode.left:
                queue.append((currNode.left, currNode))
                if currNode.left.val in to_delete:
                    currNode.left = None

            if currNode.right:
                queue.append((currNode.right, currNode))
                if currNode.right.val in to_delete:
                    currNode.right = None

        return forest

                
