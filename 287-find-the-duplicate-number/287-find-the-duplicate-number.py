class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # assigning slow and fast pointers to starting number of LL
        slow, fast = nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
                
        # Setting a new pointer from start of the LL and finding the start node of cycle in the LL
        start_slow = nums[0]
        while True:
            if(slow==start_slow):
                return slow
            slow = nums[slow]
            start_slow = nums[start_slow]
            
            
            
            