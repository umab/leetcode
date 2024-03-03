class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack[-1] + substr
                    stack.pop()
                stack.pop() # pop the open bracket

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                n = int(num)
                stack.append(n*substr) # n times substr will be appended to stack
        return "".join(stack)
        # time complexity is complex to calculate
