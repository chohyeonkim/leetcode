class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [7,1,5,3,6,4]
        #   b s b s

        # [1 5 5 5 7]

        # 1) i < i + 1  buy
        # 2) i > i + 1 sell

        stock = None
        acc = 0

        for i in range(len(prices) - 1):

            if stock == None and prices[i] < prices[i + 1]:
                stock = prices[i]

            elif stock != None and prices[i] > prices[i + 1]:
                acc = acc + prices[i] - stock
                stock = None

            print(acc)
            print(stock)

        if stock != None and stock < prices[-1]:
            acc = acc + (prices[-1] - stock)

        return acc
