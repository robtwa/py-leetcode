import pytest

from app.DynamicProgramming.climbing_stairs_70 import Solution

solver = Solution()

def test_1():
    n = 2
    expected = 2
    assert solver.climbStairs(n) == expected

def test_2():
    n = 3
    expected = 3
    assert solver.climbStairs(n) == expected

def test_3():
    n = 4
    expected = 5
    assert solver.climbStairs(n) == expected

