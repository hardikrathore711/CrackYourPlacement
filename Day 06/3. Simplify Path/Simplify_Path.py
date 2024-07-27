class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split('/')
        stack = []
        for obj in splitted:
            if obj=="" or obj==".":
                continue
            elif obj=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(obj)
        return "/"+"/".join(stack)