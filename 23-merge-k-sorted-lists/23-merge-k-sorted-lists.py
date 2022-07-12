# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists or len(lists)==0):
            return None
        while(True):
            mergedLists = []
            currLength = len(lists)
            for i in range(0,currLength,2):
                if(i+1<currLength):
                    mergedLists.append(self.mergeLists(lists[i],lists[i+1]))
                else:
                    mergedLists.append(lists[i])
            lists = mergedLists
            if(len(lists)==1):
                break
        return lists[0]
        
        
        
    def mergeLists(self,l1,l2):
        if(l1==None):
            return l2
        if(l2==None):
            return l1
        res = ListNode()
        curr = res
        while(l1 and l2):
            if(l1.val<l2.val):
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return res.next
                
            
        