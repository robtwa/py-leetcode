import pytest

from app.Graph_BFS.number_of_islands_200 import Solution

solver = Solution()


def test1():
    assert solver.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1

def test2():
    assert solver.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3

def test3():
    assert solver.numIslands([
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "0", "0"],
        ["0", "1", "1", "0", "0"],
        ["1", "0", "0", "1", "1"]
    ]) == 4

