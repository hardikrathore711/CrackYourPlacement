class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)
        zero = zero_head
        one = one_head
        two = two_head
        while head:
            temp = head.next
            head.next = None
            if head.data==0:
                zero.next = head
                zero = zero.next
            elif head.data==1:
                one.next = head
                one = one.next
            elif head.data==2:
                two.next = head
                two = two.next
            head = temp
        one.next = two_head.next
        zero.next = one_head.next
        return zero_head.next