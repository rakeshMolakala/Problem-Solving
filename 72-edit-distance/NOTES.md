Here we do the string matching for word2 with word1, if the characters match, theres no operation need to be done.
​
If they do not match we have three possibilities,
insert, we insert the word2[j] char in the position of word1[i] and move to next part recur(i,j-1)
delete, we delete the word1[i] and move to next part recur(i-1,j)
replace , we replace the word1[i] with  word2[j] and match them and move to next part
​
we find the min of these operations.
​