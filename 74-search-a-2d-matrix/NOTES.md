Here the matrix is sorted when written from left to right and top to bottom
So instead of traversing and storing into an array, we assume their positions via indices and do the binary search
​
Eg: 2x3 matrix indices are written as
​
0 1 2
3 4 5
​
so for a index number k,
row index = k//cols
col index = k%cols
​