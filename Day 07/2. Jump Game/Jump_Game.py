class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mcurr = 0
        curr = 0
        while curr<=mcurr:
            if curr>=len(nums)-1:
                return True
            mcurr = max(mcurr,curr+nums[curr])
            curr+=1
        return curr>=len(nums)