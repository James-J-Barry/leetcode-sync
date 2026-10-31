class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
        
        
        
        # @cache
        # def f(n):
        #     if n <= 1:
        #         return 1
        #     return f(n-1) + f(n-2)
        # return f(n)