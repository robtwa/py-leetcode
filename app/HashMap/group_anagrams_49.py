"""
49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List

class Solution:
    """
    I use the sorted version of each string as the hashmap key.
    Because anagrams contain the same characters, their sorted forms will always be identical.
    For example, both ‘eat’ and ‘tea’ become ‘aet’ after sorting, so they are grouped together.

    The sorting-based solution is clean and intuitive, but sorting each string costs O(k log k).
    If the input only contains lowercase English letters, I can optimize further by using a 26-character frequency array as the hashmap key.
    This reduces the overall complexity to O(nk).
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:dict[int, list[int]] = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        res =[]
        for v in groups.values():
            res.append(v)

        return res