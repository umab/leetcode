class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        mul = 1

        for i in range(len(nums)):
            arr[i] *= mul
            mul *= nums[i]
        
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= mul
            mul *= nums[i]
        return arr 