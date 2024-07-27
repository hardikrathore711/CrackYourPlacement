class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = []
        high = prices[:]
        maxx,minn = prices[-1],prices[0]
        ans = 0
        for num in prices:
            minn = min(minn,num)
            low.append(minn)
        for i in range(len(prices)-1,-1,-1):
            maxx = max(maxx,prices[i])
            high[i] = maxx
            ans=max(ans,high[i]-low[i])
        return ans
