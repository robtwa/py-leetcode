# File: test_kth_largest.py
import pytest
from app.TopK.kth_largest_element_215 import Solution

solver = Solution()

# This code uses pytest's parametrize feature to test the findKthLargest function
# with multiple test cases. Each tuple (nums, k, expected) represents one test case.
# pytest will automatically run the test function multiple times with different inputs.
@pytest.mark.parametrize("nums,k,expected", [
    ([3, 2, 1, 5, 6, 4], 2, 5),             # Find the 2nd largest element → expected result is 5
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),    # Find the 4th largest element → expected result is 4
    ([1], 1, 1),                            # Find the 1st largest element in a single-element array → expected result is 1
    ([2, 1], 1, 2),                         # Find the 1st largest element → expected result is 2
    ([7, 6, 5, 4, 3, 2, 1], 5, 3),          # Find the 5th largest element in a descending array → expected result is 3
])

def test_find_kth_largest(nums, k, expected):
    assert solver.findKthLargest(nums[:], k) == expected

