class main:
    def counter(customerWaitTimes,k):
        checkoutLines = [0]*k
        for wait in customerWaitTimes:
            minTime = min(checkoutLines)
            index = checkoutLines.index(minTime)
            checkoutLines[index] += wait
        print(max(checkoutLines))
    counter([3,10,8,7,5],2)

    
