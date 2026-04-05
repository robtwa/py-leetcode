import pytest

from app.HashMap.longest_consecutive_scequence_128 import Solution

solver = Solution()

def test_01():
    assert solver.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

def test_02():
    assert solver.longestConsecutive([1,0,1,2]) == 3


