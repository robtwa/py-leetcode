import pytest
from app.BinarySearch.koko_eating_bananas_875 import Solution

solver = Solution()

def test_1():
    assert solver.minEatingSpeed([3,6,7,11], 8) == 4

def test_2():
    assert solver.minEatingSpeed([30,11,23,4,20], 5) == 30

def test_3():
    assert solver.minEatingSpeed([30,11,23,4,20], 6) == 23
    