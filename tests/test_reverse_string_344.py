import pytest

from app.reverse_string_344 import Solution

solver = Solution()

def test_1():
    s = ["h","e","l","l","o"]
    solver.reverseString(s)
    assert s == ["o","l","l","e","h"]

def test_2():
    s = ["H","a","n","n","a","h"]
    solver.reverseString(s)
    assert s == ["h","a","n","n","a","H"]

