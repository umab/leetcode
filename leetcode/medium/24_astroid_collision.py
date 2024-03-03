class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i, astroid in enumerate(asteroids):
            while stack and astroid < 0 and stack[-1] > 0:
                diff = astroid + stack[-1]
                if diff > 0:
                    # top of stack is +ve
                    astroid = 0
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    astroid = 0
            if astroid != 0:
                stack.append(astroid)

        return stack