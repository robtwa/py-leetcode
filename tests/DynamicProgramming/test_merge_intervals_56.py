import pytest

from app.DynamicProgramming.merge_intervals_56 import Solution

solver = Solution()

def test_1():
    assert solver.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_2():
    assert solver.merge([[1,4],[4,5]]) == [[1,5]]

def test_3():
    assert solver.merge([[4,7],[1,4]]) == [[1,7]]


