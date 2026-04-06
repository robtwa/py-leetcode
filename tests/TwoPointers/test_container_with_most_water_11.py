import pytest

from app.TwoPointers.container_with_most_water_11 import Solution

solver = Solution()

def test_01():
    assert solver.maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_02():
    assert solver.maxArea([1,1]) == 1
