class main:
    def __init__(self):
        self.encoded = {}
        self.decoded = {}
        self.base = "google.com"

    def encode(self, longUrl: str) -> str:
        shortUrl = self.base + str(len(longUrl)+1)
        self.encoded[longUrl] = shortUrl
        self.decoded[shortUrl] = longUrl
        return shortUrl
    

    def decode(self, shortUrl: str) -> str:
        if shortUrl not in self.decoded:
            return ""
        return self.decoded[shortUrl]
