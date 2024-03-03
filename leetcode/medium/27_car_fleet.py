class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorting all the cars wrt to their start time.
        pair = [ [p,s] for p,s in zip(position, speed) ]
        stack = []
        for p,s in sorted(pair)[::-1]: # this is special. pay attention to this. this is not reverse sort
            stack.append((target - p)/s) # keep only 1 /. keep the division float.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
