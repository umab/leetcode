
class main:
    def majority(nums):
        table = {}
        maximum = float("-infinity")
        maxnum = 0


        for n in nums:
            table[n] = 1 + table.get(n, 0)
            if maximum < table[n]:
                maxnum = n
                maximum = table[n]
        return maxnum