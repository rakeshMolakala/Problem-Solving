Here the brute force is O(n^2) time
​
But we need to do in O(n) time. For this we maintain a HashMap of character to its index and also a start pointer indicating the starting point of the substring we are currently considering.
​
So for every character we are iterating, if the character is not seen before we calcuate the length of substring in our res and add it to our HashMap.
​
But if we see the same character again we see if the previous character is before the start character or not. If it is after our start we need move our start to next position of the prev repeated character saying it will be the new start of the substring we are considering.
​
We calcuate the max of res at every step, and this is the answer