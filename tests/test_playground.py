import pytest

from app.playground import Playground

solver = Playground()

def test1():
    assert solver.solution() == True



