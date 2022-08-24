# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # finding middle node
        slow = head
        fast = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            
        # now slow is at the middle node
        # now we reverse the linked list from middle to last
        
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # now as the second half is reversed, we use two pointers technique and come from front and back and check the values are same or not
        
        left = head
        right = prev
        while(right):
            if right.val!=left.val:
                return False
            left = left.next
            right = right.next
        return True
        
        
        
        
        

        