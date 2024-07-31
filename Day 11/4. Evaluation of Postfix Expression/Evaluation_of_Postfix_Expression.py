class Solution:
    
    def evaluatePostfix(self, S):
        stack = []
        for ch in S:
            if ord(ch)>=48 and ord(ch)<=57:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch=="+":
                    stack.append(a+b)
                elif ch=="-":
                    stack.append(a-b)
                elif ch=="*":
                    stack.append(a*b)
                elif ch=="/":
                    stack.append(a//b)
        return stack[-1]