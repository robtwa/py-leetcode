"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This algorithm finds the length of the longest consecutive sequence in
        an unsorted array. The sequence does not need to be contiguous in the
        original array. It uses a hash set for O(1) lookups and only expands
        sequences starting from valid sequence "starting points", achieving O
        (n) time complexity.

        The algorithm checks whether current_num - 1 exists in the set. If it
        does not, then current_num is the starting point of a sequence. It then
        continues to check current_num + 1, current_num + 2, and so on, until
        the sequence no longer exists. During this process, it calculates the
        length of the sequence and updates the maximum length found.
        """
        if not nums:
            return 0 # Returns 0 if nums is

        longest = 1 # Set default longest
        num_set = set(nums) # Create a set from the input list to allow for O(1) lookups

        for num in nums: # Iterate through each number in the input list
            if num - 1 not in num_set: # If num-1 is not in the set,
                # then num is the start of a sequence
                current_num = num
                current_streak = 1

                # Keep extending the sequence as long as the next number exists in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak) # Update longest

        return longest


