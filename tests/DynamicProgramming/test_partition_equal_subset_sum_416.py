import pytest

from app.DynamicProgramming.partition_equal_subset_sum_416 import Solution

solver = Solution()

def test_1():
    assert solver.canPartition([1,5,11,5]) == True

def test_2():
    assert solver.canPartition([1,2,3,5]) == False

def test_3():
    assert solver.canPartition([1,2,3,4]) == True

def test_4():
    assert solver.canPartition([1,2,3]) == True

