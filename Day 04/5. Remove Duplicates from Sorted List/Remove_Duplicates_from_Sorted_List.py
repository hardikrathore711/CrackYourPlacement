# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        while head:
            x = head.val
            temp = head
            while temp and temp.val==x:
                temp = temp.next
            head.next = temp
            head = temp
        return start
