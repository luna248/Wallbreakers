class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        retArr = []
        if n==0:
            return retArr

        if n%2==0:
            for i in range(n//2):
                retArr.append(-i-1)
                retArr.append(i+1)
        else:
            retArr.append(0)
            n=n-1
            for i in range(n//2):
                retArr.append(-i-1)
                retArr.append(i+1)

        return retArr
