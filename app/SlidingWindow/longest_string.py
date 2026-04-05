#
class Solution:
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
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This function calculates the length of the longest substring
        without repeating characters using a sliding window approach.
        It maintains a window with two pointers (left and right) and
        a set to track unique characters in the current window.

        O(n) time complexity, where n is the length of the input string s,
        because each character is visited at most twice (once by the right
        pointer and once by the left pointer).

        """

        if not s:
            return 0 # Returns 0 if s is empty

        left = 0    # The left pointer of the sliding window
        right = 0   # The right pointer of the sliding window
        max_length = 0  # Track the maximum substring length
        char_set = set() # A set to store unique characters in the current window

        while right < len(s): # Iterate until the right pointer reaches the end of the string
            if s[right] not in char_set: # If the character at the right pointer is not in the set
                char_set.add(s[right])  # Add the character to the set
                right += 1              # Move the right pointer to the right
                max_length = max(max_length, right - left) # Update the maximum length of substring
            else: # If the character at the right pointer is already in the set
                char_set.remove(s[left]) # Remove the character at the left pointer from the set
                left += 1                # Move the left pointer to the right

        return max_length
