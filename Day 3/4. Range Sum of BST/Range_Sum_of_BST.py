# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def traverse(node):
            nonlocal summ,low,high
            if not node:
                return
            if node.val>=low and node.val<=high:
                summ+=node.val
                traverse(node.left)
                traverse(node.right)
            elif node.val>=low:
                traverse(node.left)
            elif node.val<=high:
                traverse(node.right)
        

        traverse(root)
        return summ