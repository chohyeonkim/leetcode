class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.stack = []  # pair (val, span)

    def next(self, price: int) -> int:
        self.stocks.append(price)
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))

        print(self.stack)

        return span


# [100 80 60 70 60 75 85]
#   1  1  1  2   1  4  6
#   0  1  2  3  4   5  6
# by default = 1
# current_index - greater number index
# go backward
# find the next greater number


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
