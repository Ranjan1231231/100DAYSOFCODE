"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 """
class Solution:
    def solve(self, n):
        if n == 0:
            return 1

        if n < 0:
            return 0

        return self.solve(n - 1) + self.solve(n - 2)

    def solve_mem(self, n, dp):
        if n == 0:
            return 1

        if n < 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.solve_mem(n - 1, dp) + self.solve_mem(n - 2, dp)
        return dp[n]

    def solve_tab(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs(self, n: int) -> int:
        return self.solve_tab(n)
        
