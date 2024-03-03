class main:
    def prefix(strs):
        res = ""

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        for i in range(len(strs[0])):
            for s in strs:
                print(i)
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        if res:
            return res
        else:
            return ""