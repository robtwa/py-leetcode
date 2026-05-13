"""
76. Minimum Window Substring
Hard
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window. If there is no such substring, return
the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        This algorithm uses a sliding window to solve the minimum window substring problem.
        First, count the required frequency of each character in t and record how many unique characters must be satisfied.
        Use two pointers to expand the window, tracking character frequencies and how many requirements are met.
        When the window satisfies all conditions, shrink the left boundary to find a smaller valid window.
        If shrinking breaks the condition, continue expanding the right pointer.
        Finally, return the smallest valid substring, or an empty string if none exists.
        """
        if not s or not t:
            return ""  # Return empty if input invalid

        dict_t = {} # Count frequency of each char in t
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        left, right = 0, 0      # Sliding window pointers
        required = len(dict_t)  # Number of unique chars required
        formed = 0              # Number of chars that meet required frequency
        window_counts = {}      # Store current window character counts
        ans = float("inf"), None, None     # Create a Tuple to store (window length, left, right)

        # Iterate untile the right pointer reach the end of s
        while right < len(s):
            character = s[right] # Current character at right pointer
            window_counts[character] = window_counts.get(character, 0) + 1  # Add character to window count

            # If the character is in t and its count in the current window matches the required count, increment formed
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try to shrink window if valid
            while left <= right and formed == required:
                character = s[left]                 # Character at left pointe
                length = right - left + 1
                if length < ans[0]:
                    ans = (length, left, right) # Update smallest window
                window_counts[character] -= 1  # Remove left char from window
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                left += 1  # Move left pointer forward

            right += 1  # Expand window to the right

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]  # Return result substring or empty