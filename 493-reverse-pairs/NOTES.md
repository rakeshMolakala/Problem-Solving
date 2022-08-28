This problme is similar to count inversions in coding ninjas. Here in brute force we could do in O(n2) which should be optmized
​
So we use merge sort technique here.
While merging we will have two sorted arrays, then we will find the number of reverse pairs possible using two pointer technique
​
-- the two pointer technique used is critical here
we keep two pointers on i, j on left half and right half
first we iterate until i becomes exhausted, next in this iteration we iterate through j until the given condition fails, which says that j elements before satisfied our condition and we calculate that count and increments to our result
next when coming to next i element, it also checks whether j can move any forward or not, after that it also calculate the number of j elements from start of right array to j before elements.
​
Here the TC is O(nlogn) the merge fucntion complexitty is O(2n) whihc is O(n) and we make log(n) calls, so total TC is O(nlogn)
​
​