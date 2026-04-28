import pytest

from app.DynamicProgramming.longest_common_subsequence_1143 import Solution

solver = Solution()

def test_1():
    text1 = "abcde"
    text2 = "ace"
    expected = 3
    assert solver.longestCommonSubsequence(text1, text2) == expected

def test_2():
    text1 = "abc"
    text2 = "abc"
    expected = 3
    assert solver.longestCommonSubsequence(text1, text2) == expected

def test_3():
    text1 = "abc"
    text2 = "def"
    expected = 0
    assert solver.longestCommonSubsequence(text1, text2) == expected

def test_4():
    text1 = "abc"
    text2 = "ac"
    expected = 2
    assert solver.longestCommonSubsequence(text1, text2) == expected
