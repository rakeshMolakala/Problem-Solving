**Dutch flag algorith:
**
This uses a three pointer technique called low,mid,high and are initialized as follows
low = 0
mid = 0
high = n-1
​
The goal is to make the so that, [0,low-1] (inclusive) elements are all 0's
[high+1,n-1] (inclusive) elements are all 2's
​
So we try to make this array in this pattern so it will be sorted
​
The algorithm is as follows:
Note: Remember this algorithm
​
```
​
while(mid<=high):
if(nums[mid] is 0):
swap elements on low and mid
low++
mid++
if(nums[mid] is 1):
mid++
if(nums[mid] is 2):
swap elements on high and mid
high--
```
​
​
​
​