# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        j = dummy
        j.next = head
        curr = head
        x = 0
        while curr:
            x += 1
            curr = curr.next
        curr = head
        l = 0
        if x <= 1:
            return None
        while j and j.next:
            if l == x - n:
                j.next = j.next.next  
            j = j.next
            l += 1
        return dummy.next