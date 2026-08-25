class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        tabular = [0] * n
        print(len(tabular))
        tabular[0], tabular[1] = 1, 2
        for i in range(2,n):
            tabular[i] = tabular[i-1] + tabular[i-2]
        print(tabular)
        return tabular[-1]