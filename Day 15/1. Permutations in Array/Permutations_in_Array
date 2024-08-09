class Solution:
    def isPossible(self, k, arr1, arr2):
        arr1 = sorted(arr1,reverse = True)
        arr2 = sorted(arr2)
        for i in range(len(arr1)):
            if arr1[i]+arr2[i]<k:
                return False
        return True