# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        curr=head
        p=0
        q=0
        carry=0
        sm=0
        while l1!=None or l2!=None or carry==1:
            p=0 if l1==None else l1.val
            q=0 if l2==None else l2.val
            sm=p+q+carry
            digit=sm%10
            carry=sm//10
            curr.next=ListNode(digit)
            curr=curr.next
            l1=None if l1==None else l1.next
            l2=None if l2==None else l2.next
        return head.next
        