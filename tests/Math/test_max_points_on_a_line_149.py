import pytest

from app.Math.max_points_on_a_line_149 import Solution

solver = Solution()

def test_1():
    points = [[1,1],[2,2],[3,3]]
    expected = 3
    assert solver.maxPoints(points) == expected

def test_2():
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    expected = 4
    assert solver.maxPoints(points) == expected

def test_3():
    points = [[0,0],[1,1],[0,0]]
    expected = 3
    assert solver.maxPoints(points) == expected
