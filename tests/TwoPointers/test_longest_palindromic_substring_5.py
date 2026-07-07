import pytest

from app.TwoPointers.longest_palindromic_substring_5 import Solution

solver = Solution()

def test_01():
    assert solver.longestPalindrome("babad") in ["bab", "aba"]

def test_02():
    assert solver.longestPalindrome("cbbd") == "bb"

def test_03():
    assert solver.longestPalindrome("a") == "a"
