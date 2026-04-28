import pytest

from app.DynamicProgramming.longest_increasing_subsequence_300 import Solution

solver = Solution()

def test_1():
    assert solver.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

def test_2():
    assert solver.lengthOfLIS([0,1,0,3,2,3]) == 4

def test_3():
    assert solver.lengthOfLIS([7,7,7,7,7,7,7]) == 1
