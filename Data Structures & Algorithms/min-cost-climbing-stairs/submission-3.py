class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(n):
            if n == len(cost) - 1:
                return cost[n]
            if n >= len(cost):
                return 0
            return cost[n] + min(dp(n + 1), dp(n + 2))

        return min(dp(0), dp(1))