# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value=[]

        curr=head
        while curr:
            value.append(curr.val)
            curr=curr.next

        value=value[::-1]
        if value:
            head=ListNode(value[0])
            curr=head
            for right in range(1,len(value)):
                r_node=ListNode(value[right])
                curr.next=r_node
                curr=curr.next
        return head
