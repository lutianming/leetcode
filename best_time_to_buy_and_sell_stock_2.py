class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        max_profit = 0
        low = prices[0]
        profit = 0
        for i in range(n):
            p = prices[i]
            if p - low > profit:
                profit = p-low
            else:
                low = p
                max_profit += profit
                profit = 0

        max_profit += profit
        return max_profit
