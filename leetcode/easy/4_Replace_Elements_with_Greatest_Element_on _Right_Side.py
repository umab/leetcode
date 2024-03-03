class main:
    def replace(arr):
        # this solution exceed time limit for large data
        # so look at the alternate solution
        # for l in range(len(arr)):
        #     r = l + 1
        #     if r >= len(arr):
        #         arr[l] = -1
        #         return arr
        #     else:
        #         m = max(arr[r:])
        #         arr[l] = m
        # return arr

        max1 = -1
        for i in range(len(arr)-1, -1, -1):
            m = max(max1, arr[i])
            arr[i] = max1
            max1 = m
        return arr