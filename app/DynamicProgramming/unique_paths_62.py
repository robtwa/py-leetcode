"""
62. Unique Paths
Medium

There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:
1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0] * n for _ in range(m)]

        for r in range(m):
            dp[r][0] = 1

        for c in range(n):
            dp[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                # The number of ways to reach cell (r, c) is the sum of the number of ways to reach the cell:
                # 1. from the top (r-1, c)
                # 2. from the left (r, c-1)
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        # Since cells started 0 from both dimensions,
        # we need to subtract 1 from both m and n to get the correct indices.
        return dp[m-1][n-1]

