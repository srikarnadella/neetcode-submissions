class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tabular = [0] * len(cost)
        tabular[0]= cost[0]
        tabular[1] = min(cost[0] + cost[1], cost[1])
        for i in range(2, len(cost)):
            tabular[i] = min(tabular[i - 2], tabular[i-1]) + cost[i]
        print(tabular)
        return min(tabular[-1], tabular[-2])