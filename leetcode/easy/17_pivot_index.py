class main:
    def pivot(nums):
        total = sum(nums)

        leftsum = 0
        for i in range(len(nums)):
            if total - leftsum - nums[i] == leftsum:
                return i
            leftsum += nums[i]
        return -1