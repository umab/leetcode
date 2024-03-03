class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # close if there is at least 1 open
        # cannot start with close
        
        stack = []
        res = []

        def backtrack(openP, closeP):
            if openP == closeP == n:
                s = "".join(stack)
                res.append(s)
                return
            if openP < n:
                stack.append("(")
                backtrack(openP+1, closeP)
                stack.pop() # -------- why?
            if closeP < openP:
                stack.append(")")
                backtrack(openP, closeP+1)
                stack.pop() # -------- why?
        backtrack(0, 0)
        return res
