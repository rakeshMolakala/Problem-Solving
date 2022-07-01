class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        def recur(i,prev):
            if((i,prev) in cache):
                return cache[(i,prev)]
            
            res = False
            if(i==len(stones)-1):
                cache[(i,prev)] = True
                return True
            poss = [prev-1,prev,prev+1]
            j=i+1
            
            while(j<len(stones) and stones[j]-stones[i]<=prev+1):
                
                if((stones[j]-stones[i]) in poss) and  (recur(j,stones[j]-stones[i])):
                    return True
                    break
                j=j+1
                
            cache[(i,prev)] = res
            return res
                
        if(len(stones)>1 and stones[1]-stones[0]>1):
            return False
        
        cache = dict()
        return recur(1,1)
        