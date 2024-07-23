class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = [0]
        dic = {0:1}
        for i in range(len(nums)):
            presum.append(presum[-1]+nums[i])
            if (presum[-1]-k) in dic:
                ans+=dic[presum[-1]-k]
            dic[presum[-1]] = dic.get(presum[-1],0) + 1

        return ans