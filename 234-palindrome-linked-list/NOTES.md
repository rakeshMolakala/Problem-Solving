So to find the solution in O(1) space,
​
1. we first use fast and slow pointer technique to find the middle node of the linked list, that is by the time fast pointer becomes null or reaches the end node, we are at the middle of the linkedlist.
2.  If the length is odd, we are at exactly the center node, if even we second middle node
3.  Next we reverse the linked list from middle node to end node
4.  Finally we check from left and right ends of linkedlist to see if all the values are equal
5.  The intuition is, as we reversed the half palindrome when coming from back they should be same