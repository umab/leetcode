class main:
    def pattern(pattern, s):
        tablep = {}
        tables = {}

        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for p, w in zip(pattern, words):
            if p in tablep and tablep[p] != w:
                return False
            if w in tables and tables[w] != p:
                return False
            
            tablep[p] = w
            tables[w] = p

        return True
