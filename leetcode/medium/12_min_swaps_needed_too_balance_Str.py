class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        maxCount = 0

        for i in range(len(s)):
            if s[i] == "[":
                count -= 1
            else:
                count += 1
            maxCount = max(maxCount, count)
        return (maxCount + 1)//2 # -------- take out extra 2 brackets
