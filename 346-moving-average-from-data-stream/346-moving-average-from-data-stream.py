class MovingAverage:

    def __init__(self, size: int):
        self.q = collections.deque()
        self.sum = 0
        self.size = 0
        self.cap = size

    def next(self, val: int) -> float:
        pop = 0
        if(self.cap==0):
            pop = self.q.popleft()
        else:
            self.cap-=1
            self.size += 1
        self.sum = self.sum - pop + val
        self.q.append(val)
            
#         else:
#             self.q.append(val)
#             self.sum = self.sum + val
#             self.cap-=1
            # self.size += 1
        return self.sum/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)