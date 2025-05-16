class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_numeber = 0
        max_profit = 0
        # [2,5,1,5,6,7,1]
        # min
        # max

        for price in prices:

            if price < min_price:
                min_price = price
                max_numeber = 0

            else:

                max_numeber = max(max_numeber, price)
                profit = max_numeber - min_price
                max_profit = max(max_profit, profit)
                print(f"price{price}, max_numeber{max_numeber}, max_profit{max_profit}")

        return max_profit
