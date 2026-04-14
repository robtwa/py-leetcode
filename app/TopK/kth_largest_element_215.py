"""
215. Kth Largest Element in an Array

Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

import random
from typing import List


class Solution:
    """
    This function uses the Quickselect algorithm to find the kth largest element in an array.
    It leverages the partition logic from quicksort, dividing the array into two parts,
    and recursively searching only the relevant partition based on the pivot position.

    Imagine you have many toys and want the kth largest. Pick one as a “pivot.” Put smaller ones on the left and bigger
    ones on the right. Now the pivot is in the correct position. If it’s the kth largest, you’re done; if not, only
    search the needed side and repeat until you find it.
    """

    def __init__(self):
        self.k = None
        self.nums = None

    def partition(self, left, right, pivot_index):
        # Select the pivot element
        pivot = self.nums[pivot_index]

        # Switch pivot with the rightmost element for easier processing
        self.nums[pivot_index], self.nums[right] = self.nums[right], self.nums[pivot_index]

        # store_index tracks the boundary of elements smaller than pivot
        store_index = left

        # Iterate and move elements smaller than pivot to the left
        for i in range(left, right):
            if self.nums[i] < pivot:
                # Swap current element into the left partition
                self.nums[store_index], self.nums[i] = self.nums[i], self.nums[store_index]
                store_index += 1

        # Move pivot to its final sorted position
        self.nums[right], self.nums[store_index] = self.nums[store_index], self.nums[right]

        # Return pivot's final index
        return store_index

    def quickselect(self, left, right, k_smallest):
        # If only one element remains, return it
        if left == right:
            return self.nums[left]

        # Choose a random pivot to improve average performance
        pivot_index = random.randint(left, right)

        # Partition the array around the pivot
        pivot_index = self.partition(left, right, pivot_index)

        # If pivot is at target index, return it
        if k_smallest == pivot_index:
            return self.nums[k_smallest]

        # If target is in left partition, recurse left
        elif k_smallest < pivot_index:
            return self.quickselect(left, pivot_index - 1, k_smallest)

        # Otherwise recurse right partition
        else:
            return self.quickselect(pivot_index + 1, right, k_smallest)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k

        n = len(nums)
        return self.quickselect(0, n - 1, n - k)  # k-th largest is (n-k)-th smallest
