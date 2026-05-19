import pytest
from app.TopK.top_k_frequent_elements_347 import Solution

solver = Solution()

def test_1():
    assert solver.topKFrequent([1,1,1,2,2,3], 2) in [[1,2], [2,1]]

def test_2():
    assert solver.topKFrequent([1], 1) == [1]

def test_3():
    assert solver.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2) in [[1,2], [2,1]]
    
