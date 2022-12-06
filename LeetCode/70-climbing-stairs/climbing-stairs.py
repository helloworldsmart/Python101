class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = dp[i-1] + dp[i-2]
        if n == 0:
            return 0

        dp = []
        for i in range(n):
            if i == 0:
                dp.append(1)
            elif i == 1:
                dp.append(2)
            else:
                dp.append(dp[-1] + dp[-2])

        return dp[-1]
