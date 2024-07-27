# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLL(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def addTwoNumbers(self, list1, list2):
        l1 = self.reverseLL(list1)
        l2 = self.reverseLL(list2)
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
            return self.reverseLL(summ.next)
        return summ