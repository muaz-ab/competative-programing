# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        dummy = ListNode(0,head)
        lprev , curr = dummy , head
        for i in range(left-1):
            lprev , curr = lprev.next , curr.next
        prev = None
        for j in range(right - left + 1):
            tmp = curr.next
            curr.next = prev 
            prev , curr = curr , tmp
        lprev.next.next = curr
        lprev.next = prev
        return dummy.next