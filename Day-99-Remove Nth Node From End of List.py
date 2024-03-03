"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return None

        dummy = ListNode(0)
        dummy.next = head
        count = 0

        iterate = head
        while iterate != None:
            count+=1
            iterate = iterate.next 

        count-=n
        prev = dummy
        for i in range(0 , count):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next        
