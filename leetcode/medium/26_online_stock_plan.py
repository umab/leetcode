class StockSpanner:

    def __init__(self):
        self.price_span = []

    def next(self, price: int) -> int:
        span = 1
        while self.price_span and self.price_span[-1][0] <= price:
            span += self.price_span[-1][1]
            self.price_span.pop()
        self.price_span.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)