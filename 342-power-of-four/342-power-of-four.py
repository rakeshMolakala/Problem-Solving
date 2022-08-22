class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<=0):
            return False
        x = math.log(n,2)
        if(x%2==0):
            return True
        return False
        
        