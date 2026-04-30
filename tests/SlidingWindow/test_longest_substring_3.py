import pytest

from app.SlidingWindow.longest_substring_3 import Solution

solver = Solution()

def test_1():
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3

def test_2():
    assert solver.lengthOfLongestSubstring("bbbbb") == 1

def test_3():
    assert solver.lengthOfLongestSubstring("pwwke") == 3
