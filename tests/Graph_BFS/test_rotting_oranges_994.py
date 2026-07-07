import pytest

from app.Graph_BFS.rotting_oranges_994 import Solution

solver = Solution()


def test1():
    assert solver.orangesRotting([
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]) == 4

def test2():
    assert solver.orangesRotting([
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]) == -1

def test3():
    assert solver.orangesRotting([[0,2]]) == 0

def test4():
    assert solver.orangesRotting([
        [2, 1, 1],
        [1, 1, 1],
        [1, 0, 2]
    ]) == 2

