# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur, fast = head, head
        prev = None
        while fast and fast.next:
            #i start reversing the first half of the linked list here  
            fast = fast.next.next 
            cur.next, prev, cur = prev, cur, cur.next            
        max_sum = 0
        while prev:
            max_sum = max(max_sum, prev.val + cur.val)
            prev, cur = prev.next, cur.next
        return max_sum