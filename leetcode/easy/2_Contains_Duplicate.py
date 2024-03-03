class main:
    def duplicate(arr):
        table = set()
        for i in range(len(arr)):
            if arr[i] in table:
                return True
            table.add(arr[i])
        return False

    print(duplicate([1,2,3,1]))
