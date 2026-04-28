"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

## Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

## Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


## Constraints:
1 <= n <= 45
"""

class Solution:
    # DP: 1 Memoization
    def climbStairsCal(self, n:int, memo) -> int:
        # base case
        if n == 1:
            return 1
        if n == 2:
            return 2

        # if output already exits
        if memo[n] != -1:
            return memo[n]

        memo[n] = self.climbStairsCal(n - 1, memo) + self.climbStairsCal(n-2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        return self.climbStairsCal(n, memo)

    # End of Memoization ###############################################################################################

    # DP: 2 Tabulation
    def climbStairsTabulation(self, n: int) -> int:
        if n <= 2:
            return n

        # Base cases:
        # dp[1] = 1
        # dp[2] = 2

        # dp[i] = number of ways to climb to the top of a staircase with i steps
        # dp[i] = dp[i - 1] + dp[i - 2]
        # dp[3] = dp[2] + dp[1] = 2 + 1 = 3
        # dp[4] = dp[3] + dp[2] = 3 + 2 = 5

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    # End of Tabulation ################################################################################################