# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def traverse(self,node,st):
        if not node:
            return
        st+=("->"+str(node.val))
        if not node.left and not node.right:
            self.ans.append(st[2:])
            return
        self.traverse(node.left,st)
        self.traverse(node.right,st)
    def binaryTreePaths(self, root):
        self.traverse(root,"")
        return self.ans
