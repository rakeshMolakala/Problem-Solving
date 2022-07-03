Instead of going to end and coming back, we can try a solution where we consider two people starting at position (0,0) and at each step we consider the possible moves of both people combined, and we have 4 observations here:
​
1. Both reach the end point in same number of moves because only down and right moves are available
2. We can solve this using recursion, by sending the i1,j1,i2,j2 parameters of two people, but one parameter can be reduced, because as both people start at same point, after s steps, we can write r2 = r1+c1-c2, because in each move either r,c gets a increase, hence we can write this.
3. Also, when two people are at same location, we need to consider only the cherries at that location once, we need to take care of it in our recursion,
4. Finally we can use momoisation to optimise the code.