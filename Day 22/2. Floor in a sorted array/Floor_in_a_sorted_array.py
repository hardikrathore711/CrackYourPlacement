class Solution:
    def findFloor(self,A,N,X):
        for i,num in enumerate(A):
            if num>X:
                return i-1
        return N-1