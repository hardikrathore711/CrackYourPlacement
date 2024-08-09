class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = []
        i = 0
        while i<n-3:
            j = i+1
            while j<n-2:
                l = j+1
                r = n-1
                while l<r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ==target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        left = nums[l]
                        right = nums[r]
                        while l<r and nums[l]==left:
                            l+=1
                        while l<r and nums[r]==right:
                            r-=1
                    elif summ>target:
                        right = nums[r]
                        while l<r and nums[r]==right:
                            r-=1
                    else:
                        left = nums[l]
                        while l<r and nums[l]==left:
                            l+=1
                jjj = nums[j]
                while j<n-2 and nums[j]==jjj:
                    j+=1
            iii = nums[i]
            while i<n-3 and nums[i]==iii:
                i+=1
            
        return ans
                
