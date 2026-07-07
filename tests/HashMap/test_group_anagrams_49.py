import pytest

from app.HashMap.group_anagrams_49 import Solution

solver = Solution()

def test_01():
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert solver.groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]]

def test_02():
    strs = [""]
    assert solver.groupAnagrams(strs) == [[""]]

def test_03():
    strs = ["a"]
    assert solver.groupAnagrams(strs) == [["a"]]

