class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        temp = ['a','e','i','o','u']
        dic = {'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['u','i'],'u':['a']}
        cache = dict()
        cons = 1000000007
        
        def recur(prev,n):
            if((prev,n) in cache):
                return cache[(prev,n)]
            if(n==0):
                return 1
            temp_ans = 0
            if(prev==""):
                for c in temp:
                    temp_ans = temp_ans + recur(c,n-1)
            else:
                lis = dic[prev]
                for c in lis:
                    temp_ans = temp_ans + recur(c,n-1)
            temp_ans = temp_ans%cons
            cache[(prev,n)] = temp_ans
            return temp_ans
        
        return recur("",n)
                
                
            
                
        