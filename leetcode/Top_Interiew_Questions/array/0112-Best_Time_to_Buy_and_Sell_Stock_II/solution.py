class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits = 0
        for i in range(1, len(prices)):
            gap = prices[i] - prices[i - 1]
            if gap > 0:
                profits += gap

        return profits
