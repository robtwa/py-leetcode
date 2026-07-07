"""
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Use a fixed-size sliding window.
        Count character frequencies of s1, then maintain a window of length len(s1) in s2.
        Add the right char and remove the left char while sliding.
        If frequencies match, the window is a permutation of s1.
        """
        s1_len = len(s1)
        if len(s2) < s1_len:
            return False

        # count s1 char frequency
        freq_map = {}
        for s in s1:
            freq_map[s] = freq_map.get(s, 0) + 1

        left = 0
        window_map = {}
        for right in range(len(s2)):
            window_map[s2[right]] = window_map.get(s2[right],0) + 1

            window_len = right - left + 1
            if window_len > s1_len:
                window_map[s2[left]] -= 1
                if window_map[s2[left]] == 0:
                    del window_map[s2[left]]

                left += 1

            if window_map == freq_map:
                return True

        return False