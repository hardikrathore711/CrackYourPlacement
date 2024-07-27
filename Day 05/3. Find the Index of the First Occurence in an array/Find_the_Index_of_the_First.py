class Solution:
    def checkEqual(self,s1,s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if self.checkEqual(haystack[i:i+len(needle)],needle):
                return i
        return -1