class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for ind in range(len(nums)-2):
            if ind and nums[ind]==nums[ind-1]:
                continue
            i = ind+1
            j = len(nums)-1
            while i<j:
                if nums[ind] + nums[i] + nums[j] == 0:
                    if not ans or ans[-1]!=[nums[ind],nums[i],nums[j]]:
                        ans.append([nums[ind],nums[i],nums[j]])
                    i+=1
                elif nums[ind] + nums[i] + nums[j] > 0:
                    j-=1
                else:
                    i+=1
        return ans
