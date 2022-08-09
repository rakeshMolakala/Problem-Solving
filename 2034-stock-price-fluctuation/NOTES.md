1. In the update operation we add the input tuple of (timestamp, price) into maxheap and minheap. So even the outdated tuples also reside in heaps
2. when maximum/minimum called, we use the respective heaps to check whether the top most element of heap and it's price is equal to the one in our map, if it is equal we can return it, other wise it is a outdated tuple and hence we pop it and check the next top element and continue this process until we reach the matching price.
3. The update operation takes O(logn) for pushing into heaps and for N calls it takes O(NLogN) calls
4.  For min/max calls, we pop the elements from heap until we reach the right one, so it takes O(NlogN) for single call and for N calls it takes O(N^2LogN) time. But the interesting part is atmost we will pop N-1 elements from heaps, once we pop we wont pop the same element again in the next call. So the overall TC will be O(NlogN)
5.  Space complexity will be O(N) for map and heaps
​