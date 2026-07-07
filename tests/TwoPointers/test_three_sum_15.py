import pytest

from app.TwoPointers.three_sum_15 import Solution

solver = Solution()

def test_01():
    assert solver.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

def test_02():
    assert solver.threeSum([0,1,1]) == []

def test_03():
    assert solver.threeSum([0,0,0]) == [[0,0,0]]

def test_04():
    assert solver.threeSum([0,0,0,0]) == [[0,0,0]]

def test_05():
    assert solver.threeSum([-2,0,0,2,2]) == [[-2,0,2]]
