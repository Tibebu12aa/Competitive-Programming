# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        while the head is moving with twice the speed the slow pointer moves by one 
        so when the head reaches the end the slow will be in the middle
        """
        slow  = head
        while head and head.next:
            slow = slow.next
            head = head.next.next
        return slow