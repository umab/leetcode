class main:
    def subsequesnce(s, t):
        if not s:
            return True
        if not t:
            return False
        if len(s) > len(t):
            return False
        
        l = 0
        for i in range(len(t)):
            if s[l] == t[i]:
                l += 1
            if l >= len(s):
                return True
        return False