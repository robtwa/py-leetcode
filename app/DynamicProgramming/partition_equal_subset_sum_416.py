"""
416. Partition Equal Subset Sum
Medium

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

from typing import List

class Solution:
    def canPartitionTab(self, nums: List[int]) -> bool:
        """
        This problem can be solved using dynamic programming. The idea is to determine if there exists a subset of the given array that sums up to half of the total sum of the array. If such a subset exists, then the remaining elements will also sum up to half, thus partitioning the array into two equal subsets.
        
        The steps to solve the problem are as follows:
        1. Calculate the total sum of the array. If the total sum is odd, return false because we cannot split an odd number into two equal integers.
        2. Set the target sum to be half of the total sum.
        3. Use a boolean array dp where dp[i] indicates whether a subset with sum i can be formed from the elements of the array.
        4. Initialize dp[0] to true, since a sum of 0 can always be achieved with an empty subset.
        5. Iterate through each number in the array and update the dp array in reverse order to avoid overwriting results that we still need to check.
        6. Finally, return the value of dp[target], which indicates whether a subset with the target sum can be formed.
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            print("-----")
            for j in range(target, num - 1, -1):
                # if we can make the sum j by including num (j = x + num),
                # then we can also make the sum j by excluding num (x = j - num)
                dp[j] = dp[j] or dp[j - num]
                print(f"target:{target}, num: {num}, j: {j}, dp[{j}]: {dp[j]}, dp[{j - num}]: {dp[j - num]}")

        return dp[target]

    def canPartition(self, nums: List[int]) -> bool:
        return self.canPartitionTab(nums)
