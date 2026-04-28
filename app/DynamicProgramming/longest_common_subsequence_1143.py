"""
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Example: text1 = "abc", text2 = "ac"
        m,n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        n -> columns
        m -> rows

              a  c   m
           0  0  0   0
        a  0  0  0   1
        b  0  0  0   2
        c  0  0  0   3
        n  0  1  2

        We fill the dp table from left to right and top to bottom.

        For 'a' vs 'a', we have a match, dp[1][1] = 1, and we transfer the state from dp[1][1] to dp[2][1] = 1
              a  c   m
           0  0  0   0
        a  0  1  1   1
        b  0  0  0   2
        c  0  0  0   3
        n  0  1  2


        For 'b' vs 'a', no match, we take dp[2][1] = max(dp[1][1], dp[2][0]) = 1, and we transfer the state from dp[2][1] to dp[2][2] = 1

              a  c   m
           0  0  0   0
        a  0  1  1   1
        b  0  1  1   2
        c  0  0  0   3
        n  0  1  2

        For 'c' vs 'c', we transfer the state from dp[2][1] to dp[3][1] = 1, since, we have a match, dp[3][2] = dp[2][1] + 1 = 2
              a  c   m
           0  0  0   0
        a  0  1  1   1
        b  0  1  1   2
        c  0  1  2   3
        n  0  1  2


        Finally, the length of the longest common subsequence is found at dp[m][n], which in this case is dp[3][2] = 2.
        """
        m,n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            print(f"i = {i}")
            for j in range(1, n + 1):
                print(f"\tj = {j}")
                if text1[i-1] == text2[j-1]:
                    # If the characters match, we can extend the longest common subsequence found at the previous step (i-1, j-1) by 1.
                    dp[i][j] = dp[i-1][j-1] + 1
                    print(f"\t\ttext1[{i-1}] == text2[{j-1}], dp[{i}][{j}] = dp[{i-1}][{j-1}] + 1 = {dp[i][j]}")
                else:
                    # If the characters do not match, we take the maximum of the two possibilities at the previous step.
                    # dp[i-1][j] represents the case where we ignore the current character of text1
                    # dp[i][j-1] represents the case where we ignore the current character of text2.
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                    print(f"\t\ttext1[{i-1}] != text2[{j-1}], dp[{i}][{j}] = max(dp[{i-1}][{j}], dp[{i}][{j-1}]) = {dp[i][j]}")

        return dp[m][n]

