# First approach - O(n) space
Here we use two arrays of size n to store the prefix product and suffix product of each element and finally calculate the result for every element
This take O(n) time and O(n) space.
​
# Second approach - O(1) space
Here we can optimize by using only result array as this cannot be counted as extra space we can do the problem in O(1) space.
First we use the result array to prefix products of every element in a different fashion, where res[i] includes the product of elements from index 0 to index i-1, but not including i.
After this we traverse from back of the array and calculate the suffix product by updating a variable. The right_product varibale at i indicates the product of elements from i+1 to n-1 elements, and we multiply this varibale to our res[i] which contains the left product and updates the right_product suitable to next iteration. Final res is the answer.