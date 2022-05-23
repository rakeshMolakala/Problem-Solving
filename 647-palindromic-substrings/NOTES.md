1. dp[i][j] represents string s[i:j+1]
2. For each possible substring we check it is a palindrome or not
3. For length of substring greater than 2, we check whether s[i+1][j-1] is a palindrome or not and then if s[j]==s[i] or not, if it satisfies it is a palindrome
4. As d[i][j] demands dp[i+1][j-1] we cannot fill the table from top, so we fill it from bottom and consider all the substrings