Here we can do the problem in O(n) easily
​
but to further optimise it, we need to use bianry search
as the array is sorted we use binary search to find the first and last indices of occurence of given target number
From those indices we can find the number of occurences.
So how to use Binary search to find the first and last occurences of given element is the key here.
For thar we slightly modify BS function as shown in the code
When target element is found in BS, we store the index position and, we again do the binary search in the left half to find the first occurence of target, and right half if u need the last occurence of target