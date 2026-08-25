class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningCount = 0
        '''
        for l in range(len(prices)):
            for r in range(l, len(prices)):
                runningCount = max(runningCount, prices[r] - prices[l])
        return runningCount
        '''
        runningCount = 0
        l , r = 0 , 1
        while l < len(prices) and r < len(prices):
            runningCount = max(runningCount, prices[r] - prices[l])
            if prices[r] < prices[l]:
                r +=1
                l = r - 1
            else:
                r+=1
        return runningCount
            

        