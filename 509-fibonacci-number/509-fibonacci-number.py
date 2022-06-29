class Solution:
    
    dic = {0:0, 1:1}
    
    def fib(self, n: int) -> int:
        if(n in self.dic):
            return self.dic[n]
        self.dic[n] = self.fib(n-1)+self.fib(n-2)
        return self.dic[n]
        