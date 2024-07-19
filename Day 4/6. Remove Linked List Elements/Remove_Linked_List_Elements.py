# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new = ListNode(0)
        start = new
        while head:
            if head.val==val:
                head = head.next
            else:
                new.next = ListNode(head.val)
                new = new.next
                head = head.next
        return start.next