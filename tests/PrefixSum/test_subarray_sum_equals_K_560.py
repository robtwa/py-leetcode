import pytest
from app.PrefixSum.subarray_sum_equals_K_560 import Solution

solver = Solution()

def test_1():
    assert solver.subarraySum([1, 1, 1], 2) == 2

def test_2():
    assert solver.subarraySum([1, 2, 3], 3) == 2

def test_3():
    assert solver.subarraySum([1, 2, 3, 1, 2], 3) == 3
