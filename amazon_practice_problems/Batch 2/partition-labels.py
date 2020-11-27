class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partitions=[]

        ref = {char:lastFoundAt for lastFoundAt, char in enumerate(S)}
        startAt=0
        stopAt=0
        for index, char in enumerate(S):
            #we need to stop at the last found value of the character
            stopAt= max(stopAt, ref[char])
            if index==stopAt:
                partitions.append(stopAt-startAt + 1)
                startAt = index+1

        return partitions
