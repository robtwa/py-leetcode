"""
5. Longest Palindromic Substring
Medium
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    """
    I use the expand-around-center approach.

    A palindrome mirrors around its center, so for every index, I try expanding outward in two cases:
        - odd-length palindrome
        - even-length palindrome

    While the characters match, I keep expanding and update the longest palindrome found.
    """
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1

        for i in range(len(s)):
            left, right = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i + 1)

            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left

            if right2 - left2 + 1 > max_len:
                max_len = right2 - left2 + 1
                start = left2

        return s[start: start+max_len]


    def expand(self, s:str, left: int, right:int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1
