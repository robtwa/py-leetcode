import pytest

from app.SlidingWindow.longest_string import Solution

solver = Solution()

def test_add():
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    assert solver.lengthOfLongestSubstring("pwwke") == 3



