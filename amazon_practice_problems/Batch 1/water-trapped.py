class Solution:
    def trap(self, height: List[int]) -> int:
        """ For this problem, we're going to use pointers from both sides to keep track of the
        highest wall height on either side and calculate the amount of water trapped every time
        there is a dip in the height as we iterate through the array """

        #establish the pointers and variable to keep track of the solution
        leftPointer = 0
        rightPointer = len(height)-1
        waterTrapped = 0
        highestWallLeft = 0
        highestWallRight = 0

        while leftPointer < rightPointer:
            #check for dips and add the amount of water trapped
            if highestWallLeft - height[leftPointer] > 0:
                waterTrapped += highestWallLeft - height[leftPointer]
            if highestWallRight - height[rightPointer] > 0:
                waterTrapped += highestWallRight - height[rightPointer]

            #check for increase in wallheight
            highestWallLeft = max(highestWallLeft, height[leftPointer])
            highestWallRight = max(highestWallRight, height[rightPointer])

            #progress the iteration
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1

        return waterTrapped
