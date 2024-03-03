class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        row1, row2 = grid[0].copy(), grid[1].copy()

        for i in range(cols):
            if i > 0:
                row1[i] += row1[i-1]
                row2[i] += row2[i-1]
        
        pointsRobot2 = float("inf")
        for i in range(cols):
            # if robot 1 intersects 2 rows at location i then
            # robot 2 will have the values from row1[0] -> row1[i]
            # ie. their sum will be total_row - row1[i] since our rows are cumulative sums
            # exact opposite for bottom row
            top = row1[-1] - row1[i]
            bottom = row2[i-1] if i > 0 else 0
            
            # the reson to do this in 2 steps is robot1 wants to give 
            # as less as possible to robot2 
            val = max(top, bottom)
            pointsRobot2 = min(val, pointsRobot2)
        return pointsRobot2
