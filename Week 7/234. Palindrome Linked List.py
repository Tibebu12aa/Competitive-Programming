# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # check whether the singly liked list is a palindrome or not 
        # return true or false
        
        # iterate each value in the linked list
        # add the values to the stack
        # create another stack1 and if the reverse of the stack is same as stack1 then we return true else we return fasle
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next 
        stack1=[]
        for i in range(len(stack)-1,-1,-1):
            stack1.append(stack[i])
        return stack ==stack1        