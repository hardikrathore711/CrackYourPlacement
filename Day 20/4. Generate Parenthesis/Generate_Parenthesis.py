class Solution:
    def __init__(self):
        self.ans = []
    def fun(self,p,q,l,s):
        if p and not q:
            return
        if l==0 and not p and q:
            return
        if not p and not q:
            self.ans.append(s)
            return
        s1 = s
        s2 = s
        if p:
            s1+="("
            self.fun(p-1,q,l+1,s1)
        if q and l>0:
            s2+=")"
            self.fun(p,q-1,l-1,s2)

        
    def generateParenthesis(self, n: int):
        p,q = n,n
        self.fun(p,q,0,"")
        return self.ans