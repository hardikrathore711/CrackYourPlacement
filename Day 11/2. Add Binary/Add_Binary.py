class Solution:
    def addBinary(self, a, b):
        n,m = len(a),len(b)
        if m>n:
            a,b = b,a
            n,m = m,n
        carry = 0
        i,j = n-1,m-1
        ans = ""
        while i>=0 or j>=0 or carry:
            s = carry
            if i>=0:
                s+=int(a[i])
                i-=1
            if j>=0:
                s+=int(b[j])
                j-=1
            ans = str(s%2) + ans
            carry = s//2
        return ans

            
        
