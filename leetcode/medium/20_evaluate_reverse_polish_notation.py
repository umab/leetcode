class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i, c in enumerate(tokens):
            if c == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif c == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            elif c == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                print("(", val2, "/", val1, ")")
                stack.append(int(val2 / val1)) # -------- this typecasting is very imp int()
            elif c == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            else:
                stack.append(int(c))
        return stack[0]
            