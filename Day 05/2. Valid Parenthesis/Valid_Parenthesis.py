class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ord(ch)==40 or ord(ch)==91 or ord(ch)==123:
                stack.append(ord(ch))
            elif not stack:
                return False
            else:
                if abs(stack[-1]-ord(ch))<=2:
                    stack.pop()
                else:
                    return False
        return len(stack)==0