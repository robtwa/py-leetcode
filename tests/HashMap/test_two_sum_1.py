import pytest

from app.HashMap.two_sum_1 import Solution

solver = Solution()

def test_01():
    assert solver.twoSum([2,7,11,15], 9) == [0,1]

def test_02():
    assert solver.twoSum([3,2,4], 6) == [1,2]

def test_03():
    assert solver.twoSum([3,3], 6) == [0,1]

def test_04():
    assert solver.twoSum([0,4,3,0], 0) == [0,3]

def test_05():
    assert solver.twoSum([-1,-2,-3,-4,-5], -8) == [2,4]

