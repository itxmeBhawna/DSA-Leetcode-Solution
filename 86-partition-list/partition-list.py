# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        tail1 = dummy1
        tail2 = dummy2
        cur = head
        while cur:
            if cur.val < x:
                tail1.next = cur
                tail1 = tail1.next
            else:
                tail2.next = cur
                tail2 = tail2.next
            cur = cur.next
        tail1.next = dummy2.next
        tail2.next =None
        return dummy1.next            
        