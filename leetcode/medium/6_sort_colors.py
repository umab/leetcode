class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
            
        data = {}
        l = 0
        r = len(nums)-1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i]==2:
                swap(r, i)
                r -= 1
                i -= 1 # ----------------------> very imp. dont increment i when decrementing r
            i += 1
            print(l, " ", r, " ", i, " ", nums)
        