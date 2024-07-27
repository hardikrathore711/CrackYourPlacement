class Solution:
    def countBits(self, n):
        dp = [0,1]
        while len(dp)<n+1:
            temp = []
            for num in dp:
                temp.append(num+1)
            dp.extend(temp)
        return dp[:n+1]