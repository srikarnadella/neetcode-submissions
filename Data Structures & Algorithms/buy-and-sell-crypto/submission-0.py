class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningCount = 0
        for l in range(len(prices)):
            for r in range(l, len(prices)):
                runningCount = max(runningCount, prices[r] - prices[l])
        return runningCount
        