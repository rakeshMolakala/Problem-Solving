violation occurs when nums[i-1]>nums[i]
​
in this case, if we already has a violation before we can return false, otherwise it is our first violation and we need to change one of the i,i-1 element to remove the violation. This can be done in two ways:
​
1) making nums[i-1] smaller enough so that it just removes violation, which is nums[i-1]=nums[i], this can only be done if after this change the whole array before nums[i-1] is also in non decresing order. So we only do this, if nums[i-2]<=nums[i]
​
2) Doing 1 change is our first priortiy, if it doesn't happen due to nums[i-2] element, we need to increase the nums[i] element just enough to remove the violation, which is making nums[i]=nums[i-1]
​