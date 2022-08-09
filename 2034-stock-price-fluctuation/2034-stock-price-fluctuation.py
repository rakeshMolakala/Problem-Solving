import heapq
class StockPrice:

    def __init__(self):
        self.map = collections.defaultdict()
        self.curr = 0
        self.minheap = []
        self.maxheap = []
        
    def update(self, timestamp: int, price: int) -> None:
        self.map[timestamp] = price
        self.curr = max(self.curr, timestamp)
        
        heapq.heappush(self.minheap,(price,timestamp))
        heapq.heappush(self.maxheap,(-price,timestamp))

    def current(self) -> int:
        return self.map[self.curr]
        
    def maximum(self) -> int:
        price,timestamp = self.maxheap[0]
        
        while(-price!=self.map[timestamp]):
            heapq.heappop(self.maxheap)
            price,timestamp = self.maxheap[0]
        
        return -price
                
    def minimum(self) -> int:
        price,timestamp = self.minheap[0]
        
        while(price!=self.map[timestamp]):
            heapq.heappop(self.minheap)
            price,timestamp = self.minheap[0]
        
        return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()