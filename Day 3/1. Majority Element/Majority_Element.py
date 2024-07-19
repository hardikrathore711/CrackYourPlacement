class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        occ = 1
        for i in range(1,len(nums)):
            print(occ)
            if ele!=nums[i]:
                occ-=1
            else:
                occ+=1
            if occ<=0:
                occ = 1
                ele = nums[i]
        return ele