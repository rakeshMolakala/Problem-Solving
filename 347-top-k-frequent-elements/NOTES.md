**First approach using heaps:
**
TC - O(n) + O(n) + klog(n)
SC - O(n)
​
**Second approach using bucket sort:
**
Here we keep an array with maximum length of len(num)+1, because we use this array indices as the count frequency and every element in this array contains a list of elements having this count frequency i. So if we need top k freq elements, we iterate from the back and check each index and add it to our result until k ==0.
​
TC - O(n) + O(n)
SC - O(n)