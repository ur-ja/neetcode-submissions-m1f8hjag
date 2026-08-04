class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            left = dp[i - 1]
            right = dp[i - 2]
            dp[i] = left + right

        return dp[n - 1]