class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        i = 0
        while(i<len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                i+=1
        