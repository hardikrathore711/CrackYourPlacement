class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum = 0
        dic = defaultdict(int)
        ans = 0
        for num in nums:
            ans+=dic[presum]
            dic[presum]+=1
            presum = (presum+num)%k
        ans+=dic[presum]
        dic[presum]+=1
        return ans
