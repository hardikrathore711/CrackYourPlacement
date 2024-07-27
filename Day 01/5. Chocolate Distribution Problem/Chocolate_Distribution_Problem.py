
class Solution:

    def findMinDiff(self, A,N,M):
        diff = float('inf')
        A.sort()
        for i in range(N-M+1):
            diff = min(diff,A[i+M-1]-A[i])
        return diff