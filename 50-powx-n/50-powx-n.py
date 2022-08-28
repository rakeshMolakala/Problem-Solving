class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = False
        if n<0:
            n=-n
            isNeg = True
        
        
        def recur(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            if(n%2==0):
                return recur(x*x,n//2)
            else:
                return x*recur(x,n-1)
        
        res = recur(x,n)
                
        if isNeg:
            return 1/res
        return res