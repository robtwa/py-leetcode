import pytest

from app.valid_parentheses_20 import Solution

solver = Solution()

def test_1():
    assert solver.isValid("()") == True

def test_2():
    assert solver.isValid("()[]{}") == True

def test_3():
    assert solver.isValid("(]") == False

def test_4():
    assert solver.isValid("([])") == True        
