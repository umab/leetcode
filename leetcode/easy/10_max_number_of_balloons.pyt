class main:
    def balloons(text):
        balloon = Counter("balloon")
        hashmap = Counter(text)
        
        #you cannot have more ballons in  the work than its lenght
        res = len(text) 
        for c in balloon:
            res = min(res, hashmap[c] // balloon[c])
        return res