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
        I solve this problem using the sliding window technique.

        The window range is [left, right), and I use a set called char_set to keep track of characters currently inside
        the window so that all characters remain unique.

        If s[right] is not in the set, the current window is still valid. I add the character to the set, move the right
        pointer forward, and update the maximum length.

        If s[right] already exists in the set, it means the window contains duplicates. I then shrink the window from
        the left side by removing characters from the set and moving the left pointer until the window becomes valid
        again.

        Since each character is added and removed at most once, the overall time complexity is:
        O(n)
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
