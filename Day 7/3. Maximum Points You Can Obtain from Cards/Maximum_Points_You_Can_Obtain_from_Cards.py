class Solution:
    def maxScore(self, cards, k):
        n = len(cards)
        i,j = 0,n-1
        curr = 0
        while i<k:
            curr += cards[i]
            i+=1
        i-=1
        ans = curr
        while i>=0:
            curr-=cards[i]
            curr+=cards[j]
            i-=1
            j-=1
            ans= max(ans,curr)
        return ans
