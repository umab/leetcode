class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        whcounts = {}
        for w,h in rectangles:
            whcounts[w/h] = 1+ whcounts.get(w/h, 0)
        

        count = 0
        for i in whcounts.values():
            if i > 1: # need at least 2 to make a pair
                count += (i*(i-1))//2 # this math is imp
        return count