# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        first = head
        second = head
        for _ in range(n):
            second = second.next
        if not second:
            return head.next
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = first.next.next
        return head

        