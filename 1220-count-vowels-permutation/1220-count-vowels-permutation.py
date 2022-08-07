class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        #Top down recursion approach
#         dic = {"":['a','e','i','o','u'],'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['u','i'],'u':['a']}
#         cache = dict()
#         const = 1000000007
        
#         def recur(prev,n):
#             if((prev,n) in cache):
#                 return cache[(prev,n)]
#             if(n==0):
#                 return 1
#             temp_ans = 0
#             lis = dic[prev]
#             for c in lis:
#                 temp_ans = temp_ans + recur(c,n-1)
#             temp_ans = temp_ans % const
#             cache[(prev,n)] = temp_ans
#             return temp_ans
        
#         return recur("",n)
    
        
        # Bottom up approach
        prev = {'a':1,'e':1,'i':1,'o':1,'u':1,}
        const = 1000000007
        # in each iteration for number of extra a's, e's, i's, o's, u's is stored in a map
        for i in range(2,n+1):
            a = prev['e'] + prev['i'] + prev['u']
            e = prev['a'] + prev['i']
            i = prev['e'] + prev['o']
            o = prev['i'] 
            u = prev['i'] + prev['o']
            
            prev['a'] = a % const
            prev['e'] = e % const
            prev['i'] = i % const
            prev['o'] = o % const
            prev['u'] = u % const
            
        return sum(list(prev.values())) % const
        
                
        
        
        
        