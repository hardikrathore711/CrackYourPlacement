class Solution:
    def __init__(self):
        self.ans = []
    def comb(self,ind,nums,target,candidates):
        print(nums)
        if ind==len(candidates):
            return
        new = nums[:]
        new2 = nums[:]
        new_target = target - candidates[ind]
        if new_target<0:
            return
        new.append(candidates[ind])
        if new_target==0:
            self.ans.append(new)
            return
        else:
            self.comb(ind+1,new,new_target,candidates)
        temp = candidates[ind]
        while ind<len(candidates) and candidates[ind]==temp:
            ind+=1
        self.comb(ind,new2,target,candidates)
        
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.comb(0,[],target,candidates)
        return self.ans

