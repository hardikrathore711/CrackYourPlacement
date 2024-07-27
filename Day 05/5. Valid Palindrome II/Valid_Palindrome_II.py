class Solution:
    def check(self,st):
        i,j = 0,len(st)-1
        while i<j:
            if st[i]==st[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        sup = 1
        i,j = 0,len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            elif sup==1:
                sup=0
                return self.check(s[i:j]) or self.check(s[i+1:j+1])
                # if s[i]==s[j-1]:
                #     i+=1
                #     j-=2
                # elif s[i+1]==s[j]:
                #     i+=2
                #     j-=1
                # else:
                #     return False
            else:
                return False
        return True
