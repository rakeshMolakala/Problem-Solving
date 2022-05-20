class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            temp=""
            if(i%3==0):
                temp=temp+"Fizz"
            if(i%5==0):
                temp=temp+"Buzz"
            if(temp==""):
                res.append(str(i))
            else:
                res.append(temp)
                
        return res
            
        