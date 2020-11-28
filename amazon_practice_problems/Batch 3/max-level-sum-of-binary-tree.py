# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        #For this problem we'll use a deque to keep evaluate all the nodes
        allNodes = collections.deque([(root,1)])

        maxSumLevel = 0
        currMaxSum = -float('inf')

        #Each loop will go through all the nodes on one level
        while allNodes:
            lengthAtStartOfLoop = len(allNodes)
            levelSum = 0
            currLevel = None

            #this for loop will parse through all the nodes from the same level currently
            #in the deque
            for i in range(lengthAtStartOfLoop):
                currNode, currLevel = allNodes.popleft()
                levelSum += currNode.val

                #add all children of the node to the deque
                if(currNode.left):
                    allNodes.append((currNode.left, currLevel+1))
                if(currNode.right):
                    allNodes.append((currNode.right, currLevel+1))

            #Check if greatest sum and record level if it's greater than the last
            if levelSum > currMaxSum:
                currMaxSum = levelSum
                maxSumLevel = currLevel

        return maxSumLevel
