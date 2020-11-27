class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return arr

        for i in range(1,len(arr)):
            arr[i-1] = max(arr[i:])
        arr[-1]=-1

        return arr
