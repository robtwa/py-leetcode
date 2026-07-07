import pytest

from app.BinarySearch.search_in_rotated_sorted_array_33 import Solution

solver = Solution()

def test_01():
    assert solver.search([4,5,6,7,0,1,2], 0) == 4

def test_02():
    assert solver.search([4,5,6,7,0,1,2], 3) == -1

def test_03():
    assert solver.search([1], 0) == -1

def test_04():
    assert solver.search([1], 1) == 0

def test_05():
    assert solver.search([3,1], 1) == 1

