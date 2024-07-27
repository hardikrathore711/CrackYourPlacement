# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        summ = ListNode(0)
        Sum = summ
        carry = 0
        while l1 or l2 or carry:
            curr = carry
            if l1:
                curr+=l1.val
                l1 = l1.next
            if l2:
                curr+=l2.val
                l2 = l2.next
            carry = curr//10
            Sum.next = ListNode(curr%10)
            Sum = Sum.next
        if summ.next:
            return summ.next
        return summ