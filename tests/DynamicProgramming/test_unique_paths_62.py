import pytest

from app.DynamicProgramming.unique_paths_62 import Solution

solver = Solution()

def test_1():
    m = 3
    n = 7
    expected = 28
    assert solver.uniquePaths(m, n) == expected

def test_2():
    m = 3
    n = 2
    expected = 3
    assert solver.uniquePaths(m, n) == expected

def test_3():
    m = 7
    n = 3
    expected = 28
    assert solver.uniquePaths(m, n) == expected

def test_4():
    m = 2
    n = 2
    expected = 2
    assert solver.uniquePaths(m, n) == expected