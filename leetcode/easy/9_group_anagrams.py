class main:
    def anagras(strs):
        d = defaultdict(list)


        for i, s in enumerate(strs):
            arr = [0]*26
            for j in range(len(s)):
                ascii = ord(s[j]) - ord('a')
                arr[ascii] += 1
            d[tuple(arr)].append(s)
        return d.values()