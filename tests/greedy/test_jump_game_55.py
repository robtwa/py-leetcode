import pytest

from app.Greedy.jump_game_55 import Solution
solver = Solution()

def test_1():
    nums = [2,3,1,1,4]
    assert solver.canJump(nums) == True

def test_2():
    nums = [3,2,1,0,4]
    assert solver.canJump(nums) == False

