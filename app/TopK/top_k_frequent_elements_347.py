"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List

class Solution:
    """
    I solve this problem using a combination of frequency counting and bucket sort.

    First, I build a hashmap to count how many times each number appears in the array.

    Then I create a bucket array, where the index represents the frequency.
    For example, bucket[3] stores all numbers that appear 3 times.

    After that, I place each number into its corresponding bucket based on its frequency.

    Finally, I iterate through the bucket array from high frequency to low frequency and collect elements until I have k results.

    This works well because the maximum possible frequency is at most n, so bucket sort allows us to achieve linear time complexity.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # O(n) to generate a frequency map
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # O(n) to initialize a list with n buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # O(n) to place the number to its frequency list
        for num, count in freq.items():
            bucket[count].append(num)

        # O(n) to find the top k frequent elements from the tails to the head of the bucket list
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if k == len(res):
                    return res

