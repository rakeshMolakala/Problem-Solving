This problme is similar to count inversions in coding ninjas. Here in brute force we could do in O(n2) which should be optmized
​
So we use merge sort technique here.
While merging we will have two sorted arrays, then we will find the number of reverse pairs possible using two pointer technique
​
-- the two pointer technique used is critical here
​
Here the TC is O(nlogn) the merge fucntion complexitty is O(2n) whihc is O(n) and we make log(n) calls, so total TC is O(nlogn)
​
​