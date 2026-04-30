"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This function calculates the length of the longest substring
        without repeating characters using a sliding window approach.

        It maintains a window with two pointers (left and right) and
        a set to track unique characters in the current window.

        It keeps expanding the right pointer to include new characters until a duplicate is found. When a duplicate is found, it moves the left pointer to shrink the window until the duplicate is removed.

        The maximum length of the window during this process is the length of the longest substring without repeating characters.

        O(n) time complexity, where n is the length of the input string s because each character is visited at most twice (once by the right pointer and once by the left pointer).
        """

        n = len(s)
        left, right = 0,0
        max_len = 0
        char_set = set()

        while right < n:
            if s[right] not in char_set:
                # if char at right pointer not in char_set
                char_set.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                # if char at right pointer already in char_set
                char_set.remove(s[left])
                left += 1

        return max_len
