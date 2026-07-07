"""
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Sort the array and use two pointers to find triplets that sum to zero.
        Time complexity: O(n^2) due to the nested loops.
        Space complexity: O(1) if we ignore the space used for the output list.

        This function solves the "3Sum" problem.
        Given an integer array nums, it finds all unique triplets [a, b, c]
        such that a + b + c = 0. The algorithm sorts the array first, then
        fixes one number and uses a two-pointer approach to find valid pairs,
        skipping duplicates to avoid repeated results. Time complexity is O(n^2).

        """

        nums.sort() # Sort the input array in ascending order to facilitate the two-pointer approach
        result = []
        for i in range(len(nums) - 2): # Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicate elements to avoid repeating the same triplet
                continue

            # Use two pointers to find pairs that sum to -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    # If the total is less than zero, we need a larger number, so we move the left pointer to the right
                    left += 1
                elif total > 0:
                    # If the total is greater than zero, we need a smaller number, so we move the right pointer to the left
                    right -= 1
                else:
                    # If the total is zero, we found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        # Skip duplicate elements at the left pointer to avoid repeating the same triplet
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        # Skip duplicate elements at the right pointer to avoid repeating the same triplet
                        right -= 1

                    # Move both pointers to continue searching for other pairs
                    left += 1
                    right -= 1
        return result
