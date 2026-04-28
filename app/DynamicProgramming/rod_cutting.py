"""
# Rod Cutting Problem

Given a rod of length n inches and an array price[].
price[i] denotes the value of a piece of length i.
The task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

Example 1:
Input: price[] =  [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation:  The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

Example 2:
Input : price[] =  [3, 5, 8, 9, 10, 17, 17, 20]
Output : 24
Explanation : The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.

Example 3:
Input : price[] =  [3]
Output : 3
Explanation: There is only 1 way to pick a piece of length 1.

In the rod cutting problem, the goal is to determine the maximum profit that can be obtained by cutting a rod into
smaller pieces and selling them, given a price list for each possible piece length.
The approach involves considering all possible cuts for the rod and recursively calculating the maximum profit for each
cut. For detailed explanation and approaches, refer to Rod Cutting.

"""

class Solution:
    # DP: 1 Tabulation
    def rodCuttingTab(self, price) -> int:
        n = len(price)
        dp = [0] * (n+1)

        for i in range(1, n+1):
            for j in range(1, i+1):
                temp = price[j-1] + dp[i - j]
                dp[i] = max(dp[i], temp)
                print("i:", i, ", j:", j,", temp:",temp, ",dp[i]:", dp[i])

        return dp[n]

    def rodCutting(self, price) -> int:
        return self.rodCuttingTab(price)