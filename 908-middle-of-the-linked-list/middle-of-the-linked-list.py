# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        result = 0
        while temp:
            result +=1
            temp = temp.next
        mid = result // 2
        temp = head
        for _ in range(mid):
            temp = temp.next
        return temp      

        