class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i], 0) + 1
        
        lst = []
        table = sorted(table, key=table.get, reverse=True) 
        for i in range(k):
            lst.append(table[i])
    
        return lst