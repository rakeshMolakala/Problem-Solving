class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        
        def recur(prev,curr_n):
            if curr_n==n:
                res.add(prev)
                return 
            last = prev%10
            p1 = last + k
            if p1<10:
                recur(prev*10+p1,curr_n+1)
            p2 = last - k
            if p2>=0 and p2<10:
                recur(prev*10+p2,curr_n+1)
        
        for i in range(1,10):
            recur(i,1)
            
        return list(res)
            
        