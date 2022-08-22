class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<=0):
            return False
        x = math.log(n,2)
        y = math.log(4,2)
        if(x%y==0):
            return True
        return False
        
        