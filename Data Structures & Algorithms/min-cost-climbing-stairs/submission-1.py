class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache
        def dp(n):
            if n >= len(cost) or n < 0:
                return 0

            return min(dp(n + 1), dp(n + 2)) + cost[n]

        return  min(dp(0), dp(1))