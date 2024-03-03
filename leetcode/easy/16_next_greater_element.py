class main:
    def nextGreaterElem(nums1, nums2):
        stack = []
        res = [-1]*len(nums1)
        nums1index = {}
        for i in range(len(nums1)):
            nums1index[nums1[i]] = i

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                pop = stack.pop()
                idx = nums1index[pop]
                res[idx] = cur
            if cur in nums1index:
                stack.append(cur)
        return res
    # stack solution is not intuitive
    # nums1 = [1,2,3]
    # nums1index = {1:0,2:1,3:2} - reverse of array
    # check if cur is in num1index if is, push to stack and find greate elem by looping through nums2 the pop all till empty