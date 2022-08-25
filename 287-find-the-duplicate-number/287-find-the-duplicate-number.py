class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
                
        start_slow = nums[0]
        while True:
            if(slow==start_slow):
                return slow
            slow = nums[slow]
            start_slow = nums[start_slow]
            