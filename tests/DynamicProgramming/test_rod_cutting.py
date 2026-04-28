import pytest

from app.DynamicProgramming.rod_cutting import Solution

solver = Solution()

def test_1():
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    assert solver.rodCutting(price) == 22

def test_2():
    price = [3, 5, 8, 9, 10, 17, 17, 20]
    assert solver.rodCutting(price) == 24

def test_3():
    price = [3]
    assert solver.rodCutting(price) == 3
    
