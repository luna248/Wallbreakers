class MedianFinder:

    def __init__(self):
        #We're going to maintain the lower heap with negatives so the largest number
        #is stored on top of the heap
        self.lowerHeap = []
        self.upperHeap = []


    def addNum(self, num: int) -> None:
        #By default the incoming number goes into the upper heap
        heapq.heappush(self.upperHeap, num)

        #If there's an uneven number of total elements stored, we want it to be in
        #the lower heap so that we can easily fetch the median
        if(len(self.upperHeap) > len(self.lowerHeap)):
            heapq.heappush(self.lowerHeap, -heapq.heappop(self.upperHeap))

        if((len(self.upperHeap)==len(self.lowerHeap)) and
           (-self.lowerHeap[0] > self.upperHeap[0])):
            heapq.heappush(self.upperHeap, -heapq.heappop(self.lowerHeap))
            heapq.heappush(self.lowerHeap, -heapq.heappop(self.upperHeap))


    def findMedian(self) -> float:
        if(len(self.upperHeap)==len(self.lowerHeap)):
            return (self.upperHeap[0] + (-self.lowerHeap[0]))/2
        else:
            return -self.lowerHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
