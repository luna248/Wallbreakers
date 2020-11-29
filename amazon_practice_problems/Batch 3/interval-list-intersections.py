class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        overlappingIntervals = []
        allIntervals = sorted(A+B)

        if not allIntervals:
            return []

        intervalMax = allIntervals[0][1]
        for interval in allIntervals[1:]:
            if interval[0] <= intervalMax:
                overlappingIntervals.append([interval[0]]+[min(intervalMax, interval[1])])

            intervalMax = max(intervalMax, interval[1])

        return overlappingIntervals
