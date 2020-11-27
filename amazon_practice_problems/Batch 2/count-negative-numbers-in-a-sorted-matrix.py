class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #check edge case
        if not grid:
            return 0

        numOfNegatives = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] <0:
                    numOfNegatives = numOfNegatives + (len(grid[0])- j)
                    break

        return numOfNegatives
