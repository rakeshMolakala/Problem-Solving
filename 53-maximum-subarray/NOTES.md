It is a kind of Dp problem, but also example of Kadane's algorithm
​
we maintain two variables, curr_sum, max_sum. We initialise the curr and max sum to first element in the array.
​
The algorithm states that negative sum is not needed to carry forward. So whenever we come to a new element and see if the curr_sum + nums[i] is less than nums[i], which means than curr_sum is negative and we dont need to take it forward, so we make curr_sum = nums[i], if we get greater sum we do carry it out and update the curr_sum.
​
At each iteration we update the max_sum too, which is our final answer.
​