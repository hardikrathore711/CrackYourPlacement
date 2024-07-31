class Solution:
    def __init__(self):
        self.ans = []
    def okay(self, n ,k, ind, curr):
        if ind==n+1:
            return 
        curr1 = curr[:]
        curr2 = curr[:]
        curr2.append(ind)
        self.okay(n, k, ind+1, curr1)
        if len(curr2)==k:
            self.ans.append(curr2)
            return
        self.okay(n, k, ind+1, curr2)
    def combine(self, n: int, k: int):
        self.okay(n, k, 1, [])
        return self.ans

        