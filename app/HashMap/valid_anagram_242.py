"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Anagrams are words or phrases formed by rearranging the letters of another, such as "listen" becoming "silent".

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    """
    I first check whether the two strings have the same length. If not, I can immediately return false.

    Then I use two hashmaps to count character frequencies for each string.

    Finally, I compare the two frequency maps. If they are identical, the two strings are anagrams.

    The time complexity is O(n), and the space complexity is O(k), where k is the number of unique characters.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map1 = {}
        for c in s:
            freq_map1[c] = freq_map1.get(c, 0) + 1

        freq_map2 = {}
        for c in t:
            freq_map2[c] = freq_map2.get(c, 0) + 1

        return freq_map1 == freq_map2
