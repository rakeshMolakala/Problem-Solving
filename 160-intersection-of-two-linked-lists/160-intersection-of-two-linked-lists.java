/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int la = 0;
        int lb = 0;
        ListNode a = headA;
        ListNode b = headB;
        while(a!=null){
            la++;
            a=a.next;
        }
        while(b!=null){
            lb++;
            b=b.next;
        }
        
        int temp = Math.abs(la-lb);
        if(la>lb){
            while(temp>0){
                headA=headA.next;
                temp--;
            }
        }
        else{
            while(temp>0){
                headB=headB.next;
                temp--;
            }

        }
        
        while(headA!=null && headB!=null){
            if(headA==headB){
                return headA;
            }
            headA = headA.next;
            headB = headB.next;
        }
        return null;
        
    }
}