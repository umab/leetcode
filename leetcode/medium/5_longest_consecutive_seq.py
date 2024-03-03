class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)

        for n in nums:
            # check id n-1 exists
            # if not check if n+1 exists
            if n-1 not in numsSet:
                length = 1
                while n+length in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest