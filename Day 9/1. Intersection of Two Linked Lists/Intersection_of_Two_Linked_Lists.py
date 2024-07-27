# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        currA = headA
        currB = headB
        while currA and currB:
            currA = currA.next
            currB = currB.next
        if not currA:
            currA = headB
        if not currB:
            currB = headA
        while currA and currB:
            currA = currA.next
            currB = currB.next
        if not currA:
            currA = headB
        if not currB:
            currB = headA
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
        