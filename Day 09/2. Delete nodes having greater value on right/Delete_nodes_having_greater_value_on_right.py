'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        stack = [head]
        curr = head.next
        while curr:
            while stack and curr.data>stack[-1].data:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        prev = None
        for node in stack[::-1]:
            node.next = prev
            prev = node
        return prev