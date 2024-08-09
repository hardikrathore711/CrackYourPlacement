# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mn = float('inf')
        self.curr = None
    def traverse(self,node):
        if not node:
            return
        self.traverse(node.left)
        if self.curr:
            self.mn = min(self.mn, node.val - self.curr.val)
        self.curr = node
        self.traverse(node.right) 

    def getMinimumDifference(self, root):
        self.traverse(root)
        return self.mn