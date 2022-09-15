class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        
        if n % 2 != 0:
            return []
        
        hash_map = Counter(changed)
        ans = []
        changed.sort()
        
        for i in changed:
            if hash_map[i] == 0:
                continue
            else:
                hash_map[i] -= 1
            element = 2*i
            if element in hash_map and hash_map[element] > 0:
                ans.append(i)
                hash_map[element] -= 1
        
        if len(ans) == n // 2:
            return ans
        else:
            return []