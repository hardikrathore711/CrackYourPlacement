class Solution:
    def minMoves2(self, nums):
        nums.sort()
        n = len(nums)
        if n==1:
            return 0
        elif n==2:
            return abs(nums[0]-nums[1])
        m1 = nums[n//2]
        m2 = nums[(n//2) +1]
        ans1,ans2 = 0,0
        for num in nums:
            ans1+=abs(m1-num)
            ans2+=abs(m2-num)
        if n%2==0:
            return min(ans1,ans2)
        return ans1