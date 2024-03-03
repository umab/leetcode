class main:
    def down(input):
        arr = [[0]*4 ] *4
        arr[0][1] = 10
        print(arr)

        final = []
        for i, arr in enumerate(input): 
            if arr[1] == "ON":
                prevStart = arr[0]
                continue
            else:
                op = [prevStart, arr[0]]
            final.append(op)
        print(final)

    arr = [[3, "ON"], [5, "OFF"], [9, "ON"], [10, "OFF"]]
    down(arr)

    def fullDown():
        pass