# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current_node=head
        prev=None
        while current_node:
            #hold the next node
            temp=current_node.next
            #reverse the linkedlist
            current_node.next=prev
            #go to the next node
            prev=current_node
            #update the current node 
            current_node=temp

        return prev