class main:
    def isomorphic(s, t):
        maps = {} 
        mapt = {}

        
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if (( c1  in maps and maps.get(c1) != c2) or (c2  in mapt and mapt.get(c2) != c1)):
                return False

            maps[c1] = c2
            mapt[c2] = c1
        return True