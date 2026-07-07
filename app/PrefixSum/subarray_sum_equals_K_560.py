"""
560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
[1,2], [3]

Example 3:
Input: nums = [1,2,3,1,2], k = 3
Output: 3
[1,2], [3], [1,2]


Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

from typing import List

class Solution:
    """
    I solve this problem using prefix sum and a hashmap.

    `prefix_sum` represents the cumulative sum from the beginning of the array to the current position,
    and `freq_map` stores how many times each prefix sum has appeared.

    The key insight is that if the current prefix sum is prefix_sum, and a previous prefix sum equals:
    `prefix_sum − k`
    then the subarray between those two positions has a sum of k.

    While iterating through the array, I continuously update the running prefix sum and check whether prefix_sum-k
    already exists in the hashmap.
    If it does, I add its frequency to the result because it means valid subarrays have been found.

    Finally, I store the current prefix sum in the hashmap for future iterations.
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize hash map to store prefix sum frequencies
        # Start with {0: 1} to handle subarrays starting from index 0
        freq_map = {0: 1}

        # Initialize result counter and running prefix sum
        result = 0
        prefix_sum = 0

        # Iterate through each number in the array
        for num in nums:
            # Update the running prefix sum
            prefix_sum = prefix_sum + num

            # Check if (prefix_sum - k) exists in our hash map
            # If it exists, it means there are subarrays ending at current index whose sum equals k
            result = result + freq_map.get(prefix_sum - k, 0)

            # Add current prefix sum to the hash map for future iterations
            freq_map[prefix_sum] = freq_map.get(prefix_sum, 0) + 1

        return result
