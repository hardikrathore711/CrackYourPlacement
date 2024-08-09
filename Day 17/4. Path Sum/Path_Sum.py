# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = False
    def traverse(self,node,tgt):
        if not node:
            return
        tgt = tgt - (node.val)
        if not node.left and not node.right and tgt==0:
            self.ans = True
            return
        self.traverse(node.left,tgt)
        self.traverse(node.right,tgt)

    def hasPathSum(self, root, targetSum):
        self.traverse(root,targetSum)
        return self.ans