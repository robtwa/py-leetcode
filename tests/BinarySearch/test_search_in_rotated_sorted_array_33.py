import pytest

from app.BinarySearch.search_in_rotated_sorted_array_33 import Solution

solver = Solution()

def test_01():
    assert solver.search([4,5,6,7,0,1,2], 0) == 4

def test_02():
    assert solver.search([4,5,6,7,0,1,2], 3) == -1


