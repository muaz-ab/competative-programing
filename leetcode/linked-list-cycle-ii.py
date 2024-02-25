# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        s = set()
        while curr:
            if curr in s:
                return curr
            s.add(curr)
            curr = curr.next
        return None