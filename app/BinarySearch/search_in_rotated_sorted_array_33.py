"""
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such
that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or
-1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from typing import List

class Solution:
    """
    This function searches for the index of a target value in a rotated sorted array.
    The array was originally sorted in ascending order but then rotated.
    It uses a modified binary search to achieve O(log n) time complexity.
    Core idea: determine which half is sorted, then check if the target lies within it,
    and narrow down the search range accordingly.
    """
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers to the start and end of the array
        left, right = 0, len(nums) - 1

        # Continue searching while the left pointer is less than or equal to the right pointer
        while left <= right:
            # Calculate the middle index to avoid potential overflow
            mid = (left + right) // 2

            # If the middle value equals the target, return its value
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # If the left half is sorted
                # Check if the target is in the left half
                if nums[left] <= target < nums[mid]:
                    # Move the right pointer to mid - 1 to search in the left half
                    right = mid - 1
                else:
                    # Move the left pointer to mid + 1 to search in the right half
                    left = mid + 1

            else: # If the right half is sorted
                # Check if the target is in the right half
                if nums[mid] < target <= nums[right]:
                    # Move the left pointer to mid + 1 to search in the right half
                    left = mid + 1
                else:
                    # Move the right pointer to mid - 1 to search in the left half
                    right = mid - 1

        return -1 # If the target is not found, return -1




        