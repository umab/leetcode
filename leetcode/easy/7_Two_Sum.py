class main:    
    def sum(nums, target):
        ans = {}

        # ans contains oppsite of input ie 
        # value to index data
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in ans:
                return [i, ans[diff]]
            ans[n] = i
        return