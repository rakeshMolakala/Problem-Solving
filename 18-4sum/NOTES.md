Here the optimal approach is to use i,j iterating loops and using two pointers technique for the remaining part of the target. In doing this, to avoid duplicates, we just skip the same elements until we get a different elment than prev element. This is done for all the 4 pointers.
​
TC - O(n^3)
SC - S(1)