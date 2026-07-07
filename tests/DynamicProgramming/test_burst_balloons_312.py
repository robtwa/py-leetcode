import pytest

from app.DynamicProgramming.burst_balloons_312 import Solution

solver = Solution()

def test_1():
    assert solver.maxCoins([3,1,5,8]) == 167

def test_2():
    assert solver.maxCoins([1,5]) == 10
