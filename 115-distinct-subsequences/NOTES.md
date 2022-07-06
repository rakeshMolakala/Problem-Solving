recur(i,j) represents number of distinct subsequences of string t[:j+1] in string s[:i+1], first we check if the current characters are same or not, if they are same, we have two possibilities, one to include that character of s in the subsequence or not include, if include we call recur(i-1,j-1) otherwise, we still search for t[j] in s[:i] and call recur(i-1,j).
​
if the characters are not equal, we simply call recur(i-1,j)
​
base cases:
if we have t string more than s string, we cannot find match and returns 0
if we reach j==-1, we know that all characters of t are matched and we return 1