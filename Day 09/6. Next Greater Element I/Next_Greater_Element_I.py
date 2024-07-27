class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        n = len(nums2)
        dic = {}
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                dic[nums2[i]] = stack[-1]
            else:
                dic[nums2[i]] = -1
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(dic[num])
        return ans