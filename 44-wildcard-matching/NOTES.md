Here the difficult part is to handle the *, whenever we get a star we can choose to match o chars , 1 char, 2 chars, 3 chars and so on, to do this efficiently, we will do one thing
​
We chose two ways, whether to ignore the star was there and move to recur(i,j-1) which also means star matches to a empty string and we move,
The other way is we make the star to match a single character to still use star for next match, this can done by recur(i-1,j)
​
These two possibilities can be done to handle star
​
The other difficult part is to handle base cases,
if we get j<0 and i>=0, we return False
if we get i<0 and j<0 we everything matched perfectly so return True
if we get i<0 and j>=0 , all j's should be * s so that they can match a empty string, we check that and return True if all stars or False otherwise