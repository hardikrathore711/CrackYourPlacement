# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lpath = 0
        def longestpath(node):
            nonlocal lpath
            if not node:
                return 0
            l = longestpath(node.left)
            r = longestpath(node.right)
            lpath = max(lpath,1+l+r)
            return 1+max(l,r)
        longestpath(root)
        return lpath-1