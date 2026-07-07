import pytest

from app.Graph_BFS.shortest_path import Solution

solver = Solution()

def test1():
    strArr = ["4", "A", "B", "C", "D", "A-B", "A-C", "B-C", "C-D"]
    assert solver.shortestPath(strArr) == "A-C-D"

