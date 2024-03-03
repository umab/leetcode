class main:
    #impl is merge sort
    # merge soer is most difficult
    # it works on divide and conquor phase
    # divide: keep splitting array into small sections till only 1 elem per section
    # conquor: compare and merge 

    # complexity is nlon(n)
    # for array of len n, we divide it by 2 till we have one elem each
    # ie n/(2*2*2....) = 1 => 2^pow(x) = n => log(n) =xlog(2)..
    # we can ignore log 2. this indicates height of the tree

    # at every level in tree we have all the n nums to compare and sort
    # ie n is the length
    # hence log(n) * n

    def merge_sort():
        arr = [5,2,3,4]
        def sort(arr, l , m ,r ):
            left, right = arr[l:m+1], arr[m+1: r+1]
            i,j,k = l, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i +=1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i +=1

        def sort(arr, l, r):
            if l == r:
                return arr
            
            m = (l+r)//2
            sort(arr, l, m)
            sort(arr, m+1, r)
            sort(arr, l, m, r)
            return arr
        return sort(arr, 0 , len(arr)-1)

