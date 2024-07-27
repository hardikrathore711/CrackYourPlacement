# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node1,node2):
            if not node1 and not node2:
                return None
            summ = 0
            if node1:
                summ += node1.val
            if node2:
                summ += node2.val
            node = TreeNode(summ)
            if node1 and node2:
                node.left = traverse(node1.left,node2.left)
                node.right = traverse(node1.right,node2.right)
            elif node1:
                node.left = traverse(node1.left,None)
                node.right = traverse(node1.right,None)
            else:
                node.left = traverse(None,node2.left)
                node.right = traverse(None,node2.right)
            return node
        return traverse(root1,root2)