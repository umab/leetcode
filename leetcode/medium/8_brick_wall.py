class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countgap = {0:0} # ------this is to initiate map. hypothe. if there are no gaps then 0 will be subtracted

        for row in wall:
            total = 0
            for i in row[:-1]: # --------- exclude last elem since we have 0 above and we dont want the line at the end of the wall
                total += i
                countgap[total] = 1 + countgap.get(total, 0)
        #retun max where gpas are found
        # if no gaps are found then return end of wall
        return len(wall) - max(countgap.values())
