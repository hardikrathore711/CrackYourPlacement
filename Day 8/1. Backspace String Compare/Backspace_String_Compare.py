class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2 = [],[]
        for ch in s:
            if ch=="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)
        for ch in t:
            if ch=="#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)
        str1 = "".join(stack1)
        str2 = "".join(stack2)
        return str1==str2