class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        right = 0
        stack = []

        for n in pushed:
            stack.append(n)
            while right < len(popped) and stack and stack[-1] == popped[right]:
                stack.pop()
                right += 1
        
        if not stack:
            return True
        return False