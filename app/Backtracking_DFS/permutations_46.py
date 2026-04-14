"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # the result list to store all the permutations
        n = len(nums) # length of the input list
        visited = [False] * n # a list to keep track of which elements have been used in the current path

        def backtrack(path): # a helper function to perform backtracking
            print("---")
            print("res: ", res)
            print("path: ", path)
            print("visited: ", visited)

            # Base case: when the current path has the same length as the input list, we have a complete permutation
            if len(path) == n:
                res.append(list(path)) # add a copy of the current path to the result list
                return

            # Recursion: iterate through the input list and try to build the permutation
            for i in range(n):
                if visited[i]:
                    continue

                visited[i] = True
                path.append(nums[i])
                backtrack(path) # recursively call backtrack with the updated path
                item = path.pop()
                visited[i] = False

        backtrack([])
        return res

