import pytest

from app.DynamicProgramming.largest_subset import Solution

solver = Solution()

def test_1():
    assert solver.getSubsetLength([1, 2, 3, 4], [2, 3, 5, 5]) == 3

def test_2():
    assert solver.getSubsetLength([1, 2, 2, 4], [2, 3, 5, 5]) == 4

def test_3():
    assert solver.getSubsetLength([1, 2, 3, 4], [2, 3, 4, 5]) == 3

