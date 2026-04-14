from typing import List


class Solution:
    def minimumSwap(self, nums: List[int]) -> int:
        # case 1: 0 left, 1 right -> count 1 before 0
        ones = 0
        moves1 = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                moves1 += ones

        # case 2: 1 left, 0 right -> count 0 before 1
        zeros = 0
        moves2 = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                moves2 += zeros

        print("moves1:", moves1, "moves2:", moves2)
        return min(moves1, moves2)
