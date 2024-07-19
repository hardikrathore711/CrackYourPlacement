# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def traverse(nums,l,r):
            if l==r:
                return TreeNode(nums[l])
            if l>r:
                return None
            mid = l+ (r-l)//2
            midNode = TreeNode(nums[mid])
            midNode.left = traverse(nums,l,mid-1)
            midNode.right = traverse(nums,mid+1,r)
            return midNode
        return traverse(nums,0,n-1)