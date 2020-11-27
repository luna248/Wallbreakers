class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        totalTeams=0

        for midVal in rating[1:-1]:
            infL, infR, supL, supR = 0, 0, 0, 0
            for checkLeft in rating[0:rating.index(midVal)]:
                if(checkLeft < midVal):
                    infL += 1
                else:
                    supL += 1
            for checkRight in rating[rating.index(midVal)+1:]:
                if(checkRight < midVal):
                    infR += 1
                else:
                    supR += 1

            totalTeams += (supL*infR) + (infL*supR)

        return totalTeams
