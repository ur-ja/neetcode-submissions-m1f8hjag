class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n # last row is always 1

        for c in range(m - 2, -1, -1):
            for r in range(n - 2, -1, -1):
                dp[r] += dp[r + 1]
 
        return dp[0]