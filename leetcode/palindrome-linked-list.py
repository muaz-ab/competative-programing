# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.prev = None
        self.curr = head
        li1 = []
        li2 = []
        while self.curr:
            li1.append(self.curr.val)
            next = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = next
        while self.prev:
            li2.append(self.prev.val)
            self.prev = self.prev.next

        return li1 == li2
        