class main:
    def isanagram(s, t):
        if not t:
            return True
        if not s:
            return False
        if len(s) != len(t):
            return False
        
        table = {}
        for i in range(len(s)):
            table[s[i]] = 1 + table.get(s[i],0)
        
        for i in range(len(t)):
            if t[i] not in table:
                return False
            table[t[i]] -= 1
            if table[t[i]] < 0: # this is if there is an extra char like s=aab t=aaa
                return False
        return True
    
    print(isanagram("rat", "car"))
            

