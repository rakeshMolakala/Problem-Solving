Same problem as shortest word distance question, but the function call is made multiple times. So traversing through the list from start to end in every call will cause O(N(calls)) which gives TLE.
​
So we need to reduce the O(N) to some part on every call, we can do that by preprocessing the given wordsDict. So we create a map of every word to a list containing the indices of every occurence of that word.
​
[w1,w2,w1,w3,w4,w1,w5,w3]
map = {w1:[0,2,5] ; w2:[1] ; w3:[3,6] ; .....}
​
So for a given function call for word1 and word2, we can use two pointers on two lists of these particular words to compute the minimum distance between the occurences of two words.
​
By starting at 0 index of two lists, we compute the distance and move the pointer that has less index value, so that we can reduce the distance between them. By doing this we will calculate the minimum distance between two words in O(max(m,n)) time, where m,n are length of occurences of given two words.
​
​
​
​
​
​