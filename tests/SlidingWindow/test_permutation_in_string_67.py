import pytest

from app.SlidingWindow.permutation_in_string_67 import Solution

solver = Solution()

def test_01():
    assert solver.checkInclusion("ab", "eidbaooo") == True

def test_02():
    assert solver.checkInclusion("ab", "eidboaoo") == False

def test_03():
    assert solver.checkInclusion("adc", "dcda") == True

def test_04():
    assert solver.checkInclusion("hello", "ooolleoooleh") == False
