class main:
    def trangle(numRows):
        res = [[1]]
        for i in range(numRows-1):
            prev = [0] + res[-1] + [0] #add 0 and -1 gives the last row
            newrow = []
            for j in range(len(res[-1])+1):
                newrow.append(prev[j] + prev[j+1])
            res.append(newrow)
        return res 

        # initilize base array with [1]
        # run 1st loop with i -> rows-1 (since [1] is already added)
        # temp_row = assume there is 0 at the beginning and end of each row for ease of claculation
        # run second loop for last row in len(res)+1 and add all elems in temp_row
        # execution o(n^2) and space o(n^2)