"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None

        retArr =[]
        for each in root.children:
            retArr.extend(self.postorder(each))

        return retArr+[root.val]
