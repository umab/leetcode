class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        op = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, index = stack.pop()
                op[index] = (i - index)  
            stack.append([temp, i])
        return op