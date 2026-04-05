import pytest

from app.BinarySearch.binary_search_704 import Solution

solver = Solution()

def test_01():
    assert solver.search([-1,0,3,5,9,12], 9) == 4

def test_02():
    assert solver.search([-1,0,3,5,9,12], 2) == -1


