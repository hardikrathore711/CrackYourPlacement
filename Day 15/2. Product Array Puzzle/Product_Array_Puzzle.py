class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        czero = 0
        ind = -1
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                czero+=1
                ind = i
                if czero>=2:
                    break
        ans = []
        if czero!=0:
            ans = [0]*len(nums)
            if czero==1:
                ans[ind] = prod
        else:
            for i in range(len(nums)):
                ans.append(prod//nums[i])
        return ans