class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('Inf')
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
