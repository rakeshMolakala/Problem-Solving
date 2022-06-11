class Solution(object):
    def minOperations(self, li, x):
        numsSum = sum(li)
        k = numsSum-x
        n = len(li)
        i, j, s = 0, 0, 0
        l = []
        maximum = float('-inf')
        if numsSum == x:
            return n
        if k>0:
            while j < n:
                s += li[j]
                if s < k:
                    j += 1
                elif s == k:
                    maximum = max(maximum, j-i+1)
                    j += 1
                elif s > k:
                    while s > k:
                        s -= li[i]
                        i += 1
                        if s == k:
                            maximum = max(maximum, j-i+1)
                    j += 1
            return n-maximum if maximum != float('-inf') else -1
        else: return -1