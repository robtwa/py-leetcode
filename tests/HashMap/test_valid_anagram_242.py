import pytest

from app.HashMap.valid_anagram_242 import Solution

solver = Solution()

def test_01():
    s1 = "anagram"
    s2 = "nagaram"
    assert solver.isAnagram(s1, s2) == True

def test_02():
    s1 = "rat"
    s2 = "car"
    assert solver.isAnagram(s1, s2) == False

