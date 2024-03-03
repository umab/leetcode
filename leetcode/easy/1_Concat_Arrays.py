class main:
    def concat(arr):
        if not arr:
            return []
        
        newarr = [0]*len(arr)*2
        l = len(arr)
        for i in range(len(arr)):
            newarr[i] = arr[i]
            newarr[l] = arr[i]
            l += 1
        return newarr

    print(concat([1,2,1]))

    def fasterConcat(nums):
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums