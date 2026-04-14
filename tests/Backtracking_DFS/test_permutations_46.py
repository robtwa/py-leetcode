import pytest

from app.Backtracking_DFS.permutations_46 import Solution

solver = Solution()

def test1():
    assert solver.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def test2():
    assert solver.permute([0,1]) == [[0,1],[1,0]]

def test3():
    assert solver.permute([1]) == [[1]]        

    