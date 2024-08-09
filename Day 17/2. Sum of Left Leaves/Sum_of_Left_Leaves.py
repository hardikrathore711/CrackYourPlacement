# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def traverse(self,node,lft):
        if not node:
            return
        if not node.left and not node.right and lft:
            self.sum += node.val
        self.traverse(node.left,True)
        self.traverse(node.right,False)

    def sumOfLeftLeaves(self, root):
        self.traverse(root,False)
        return self.sum