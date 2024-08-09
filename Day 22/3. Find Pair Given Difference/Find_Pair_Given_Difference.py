from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        i,j = 0,1
        arr.sort()
        while j<n:
            if arr[j]-arr[i] == x:
                return 1
            elif arr[j]-arr[i] < x:
                j+=1
            elif arr[j]-arr[i] > x:
                i+=1
            if i==j:
                j+=1
        return -1