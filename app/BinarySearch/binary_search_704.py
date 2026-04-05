"""
704. Binary Search
Easy
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """
        This function performs a binary search on a sorted array to find the index of a target value.
        It uses two pointers (left and right) to narrow down the search space by comparing the target
        with the middle element of the current search range.

        O(log n) time complexity, where n is the number of elements in the input array nums,
        because it halves the search space with each iteration.
        """

        left, right = 0, len(nums) - 1 # Initialize left and right pointers

        while left <= right: # Continue searching while the left pointer is less than or equal to the right pointer
            # (left + right) // 2 May cause integer overflow in some languages (like C/C++/Java).
            # left = 2,000,000,000
            # right = 2,100,000,000
            # (left + right) overflow
            # (right - left) safe
            mid = left + (right - left) // 2 # Calculate the middle index

            if nums[mid] == target: # If the middle element is equal to the target, return its index
                return mid
            elif nums[mid] < target: # If the middle element is less than the target, move the left pointer to mid + 1
                left = mid + 1
            else: # If the middle element is greater than the target, move the right pointer to mid - 1
                right = mid - 1

        return -1 # Return -1 if the target is not found in the array

