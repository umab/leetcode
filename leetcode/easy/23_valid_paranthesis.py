class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, p in enumerate(s):
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else:
                bracket = stack.pop() if stack else ""
                if (p == "]" and bracket != "[" or
                   p == ")" and bracket != "(" or 
                   p == "}" and bracket != "{"):
                    return False
        if stack:
            return False
        return True
