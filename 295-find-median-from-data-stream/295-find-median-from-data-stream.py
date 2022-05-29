import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,num*-1)
        heapq.heappush(self.minHeap,-1*heappop(self.maxHeap))
        if(len(self.maxHeap)+1<len(self.minHeap)):
            heapq.heappush(self.maxHeap,-1*heappop(self.minHeap))
        
    def findMedian(self) -> float:
        if(len(self.maxHeap)==0):
            return self.minHeap[0]
        elif (len(self.maxHeap)<len(self.minHeap)):
            return self.minHeap[0]
        elif len(self.maxHeap)==len(self.minHeap):
            return (self.minHeap[0]+(-1*self.maxHeap[0]))/2
        
        
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()