"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This function takes a list of integers and a target integer, and returns the indices of the two numbers in the
        list that add up to the target.

        The function uses a dictionary to store the numbers we have seen so far and their corresponding indices. As we
        iterate through the list of numbers, we calculate the complement (the number we need to find to reach the target
        ) and check if it is already in the dictionary. If it is, we have found the two numbers that add up to the
        target and we can return their indices. If it is not, we add the current number and its index to the dictionary
        and continue iterating through the list. If we finish iterating through the list without finding a solution, we
        return an empty list.
        """

        # Create a dictionary to store value -> index mappings
        seen = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that we need to find
            complement = target - num

            # Check if the complement is already in the seen dictionary
            if complement in seen:
                # If it is, we have found the two numbers that add up to the target and we can return their indices
                return [seen[complement], i]

            # If the complement is not in the seen dictionary, add the current number and its index to the dictionary
            seen[num] = i

        # If we finish iterating through the list without finding a solution, we can return an empty list
        return []
