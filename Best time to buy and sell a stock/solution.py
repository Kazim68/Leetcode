class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - small)
            small = min(small, prices[i])
        return profit