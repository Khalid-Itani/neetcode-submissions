class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        curMax = 0
        absMax = 0

        while r < len(prices):
            if prices[r] - prices[l] >= 0:
                curMax = prices[r] - prices[l]
                absMax = max(curMax, absMax)
            else:
                curMax = 0
                l = r
            r += 1
        return absMax