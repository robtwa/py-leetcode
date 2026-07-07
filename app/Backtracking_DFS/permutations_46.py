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
    """
    I solve this problem using backtracking.
    The idea is to build permutations step by step.

    path represents the current permutation being constructed, and visited keeps track of which elements have already
    been used so we do not reuse them.

    At each recursion level, I iterate through all numbers.
    If a number has already been used, I skip it. Otherwise, I add it to the current path and mark it as visited.

    Then I recursively continue building the permutation.

    When the length of path equals the input size, it means a complete permutation has been formed, so I add a copy to
    the result.

    After recursion returns, I perform backtracking by removing the last element and resetting the visited state,
    allowing the algorithm to explore other possible choices.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # the result list to store all the permutations
        n = len(nums) # length of the input list
        visited = [False] * n # a list to keep track of which elements have been used in the current path

        def backtrack(path): # a helper function to perform backtracking
            print("-"*80)
            # Base case: when the current path has the same length as the input list, we have a complete permutation
            if len(path) == n:
                res.append(list(path)) # add a copy of the current path to the result list
                print(f"base case: {path} added to {res}")
                return

            print(f"backtrack: path={path}, res={res}, visited={visited}")
            # Recursion: iterate through the input list and try to build the permutation
            for i in range(n):
                print(f"\ti={i}")
                if visited[i]:
                    print(f"\t\tskip: path={path}, visited={visited} ")
                    continue

                visited[i] = True
                path.append(nums[i])
                print(f"\t\tappend({nums[i]}), path={path}, visited={visited} ")

                backtrack(path) # recursively call backtrack with the updated path
                item = path.pop()
                visited[i] = False
                print(f"pop {item} out from path {path}, resetting visited={visited}")

        backtrack([])
        return res

