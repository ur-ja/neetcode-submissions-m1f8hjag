class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def f(i):
            if i >= n:
                return 0
            
            return cost[i] + min(f(i + 1), f(i + 2))

        return min(f(0), f(1))