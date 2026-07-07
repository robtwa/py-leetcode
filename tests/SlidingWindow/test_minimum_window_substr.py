import pytest

from app.SlidingWindow.minimum_window_substr import Solution

solver = Solution()

def test_01():
    assert solver.minWindow("ADOBECODEBANC", "ABC") == "BANC"

def test_02():
    assert solver.minWindow("a", "a") == "a"

def test_03():
    assert solver.minWindow("a", "aa") == ""

def test_04():
    assert solver.minWindow("a", "b") == ""

def test_05():
    assert solver.minWindow("abbdca", "bc") == "bdc"

def test_06():
    assert solver.minWindow("abbdcba", "bbc") == "bbdc"

def test_07():
    assert solver.minWindow("aa", "aa") == "aa"

def test_08():
    assert solver.minWindow("abaacbba", "aabc") == "baac"
