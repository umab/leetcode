class main:
    def disappear(nums):
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        res = []
        for i in range(1, len(nums)+1):
            if i not in hashmap:
                res.append(i)
        return res