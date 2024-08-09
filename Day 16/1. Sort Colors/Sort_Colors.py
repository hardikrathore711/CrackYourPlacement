class Solution:
    def sortColors(self, nums):
        z,o,t = 0,0,len(nums)-1
        while o<=t:
            print(nums)
            if nums[o]==0:
                nums[o],nums[z] = nums[z],nums[o]
                z+=1
                o+=1
            elif nums[o]==1:
                o+=1
            else:
                nums[o],nums[t] = nums[t],nums[o]
                t-=1
        
    