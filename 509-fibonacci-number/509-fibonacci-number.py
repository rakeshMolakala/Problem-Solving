class Solution:
    
    global dic
    dic = dict()
    
    def fib(self, n: int) -> int:
        if(n in dic):
            return dic[n]
        if(n==0):
            return 0
        if(n==1):
            return 1
        res = self.fib(n-1)+self.fib(n-2)
        dic[n]=res
        return res
        