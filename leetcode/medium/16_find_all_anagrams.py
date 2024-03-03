class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res = []
        table = {}
        plen = len(p)
        slen = len(s)

        def isAnagram(s,t):
            for i in range(len(s)):
                table[s[i]] = 1 + table.get(s[i], 0)
            for i in range(len(t)):
                if t[i] not in table:
                    return False
                table[t[i]] -= 1
                if table[t[i]] < 0: # this is if there is an extra char like s=aab t=aaa
                    return False
            return True
            
        for i in range(slen -plen + 1): 
            table = {}
            if isAnagram(s[i: i+plen], p):
                res.append(i)
        return res
        