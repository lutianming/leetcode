class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        max_profit = 0
        low = 0
        segs = []
        profit = 0
        for i in range(n):
            p = prices[i]
            if p - prices[low] >= profit:
                profit = p-prices[low]
            else:
                if profit > 0:
                    segs.append((low, i-1))
                    max_profit += profit
                low = i
                profit = 0
        if profit > 0:
            segs.append((low, n-1))
            max_profit += profit

        max_profit = 0
        nsegs = len(segs)

        for i in range(nsegs):
            profit = self.maxSeg(segs[0:i], prices) + self.maxSeg(segs[i:nsegs], prices)
            if profit > max_profit:
                max_profit = profit
        return max_profit

    def maxSeg(self, segs, prices):
        max_profit = 0
        min_price = float('Inf')
        for seg in segs:
            p = prices[seg[0]]
            if p < min_price:
                min_price = p
            p = prices[seg[1]]
            if p-min_price > max_profit:
                max_profit = p-min_price
        return max_profit

s = [3,3,5,0,0,3,1,4]
# s = [2,1,4]
solution = Solution()
print(solution.maxProfit(s))
