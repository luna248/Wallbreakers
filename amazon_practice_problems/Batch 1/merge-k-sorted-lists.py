# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minimumIndex = -1
        minimum = float(inf)

        for i in range(len(lists)):
            if lists[i] and lists[i].val< minimum:
                minimum = lists[i].val
                minimumIndex = i

        if minimumIndex == -1:
            return None
        else:
            finalSorted = lists[minimumIndex]
            lists[minimumIndex] = lists[minimumIndex].next
            finalSorted.next = self.mergeKLists(lists)
            return finalSorted
