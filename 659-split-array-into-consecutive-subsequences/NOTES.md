And curr be element we are currently at the array
​
Then we have three cases
​
1. curr>last+1
Then we check whether this subsequence has length 3, if it doesn’t we return false, if it has we pop up and check for the next last element from the heap and do the same process
​
2. Curr==last or heap is empty
That means we cannot find the right subsequence to add curr element, so we create a new subsequence and add it to heap
​
3. curr==last+1
This is the most obvious case, we pop the head element of the heap and update the length and last element and add it to the heap, as we are using a tuple of heaps, even though there are multiple subsequences with same last element they use the length parameter of tuple to sort, which we want.
​
Finally we check the list of subsequences to see if there are any less than length 3, if yes return false, else true
​
​