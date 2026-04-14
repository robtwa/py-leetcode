import pytest

from app.temp.unlock_maximum_sequence import Solution

solver = Solution()

def test1():
    assert solver.getOptimalSequence([10,5,7,6],'0101',2) == [6,7]

def test2():
    solver = Solution()
    assert solver.getOptimalSequence([1, 2, 100, 1, 1], '00100', 3) == [100, 100, 100]

def test3():
    solver = Solution()
    assert solver.getOptimalSequence([5, 100, 1, 1], '0100', 2) == [100, 100]

def test4():
    solver = Solution()
    assert solver.getOptimalSequence([1,2,3], "000", 3) == []

def test5():
    solver = Solution()
    assert solver.getOptimalSequence([1,5,3], "111", 3) == [5,5,5]

def test6():
    solver = Solution()
    assert solver.getOptimalSequence([1,2,3,4], "0100", 2) == [2,4]

def test7():
    solver = Solution()
    assert solver.getOptimalSequence([1,2,3,100], "0100", 2) == [2,100]
