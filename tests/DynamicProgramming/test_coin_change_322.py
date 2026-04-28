import pytest

from app.DynamicProgramming.coin_change_322 import Solution

solver = Solution()

def test_1():
    coins = [1,2,5]
    amount = 11
    expected = 3
    assert solver.coinChange(coins, amount) == expected

def test_2():
    coins = [2]
    amount = 3
    expected = -1
    assert solver.coinChange(coins, amount) == expected

def test_3():
    coins = [1]
    amount = 0
    expected = 0
    assert solver.coinChange(coins, amount) == expected

def test_4():
    coins = [1, 2, 3]
    amount = 7
    expected = 3
    assert solver.coinChange(coins, amount) == expected

def test_5():
    coins = [2, 3, 5]
    amount = 7
    expected = 2
    assert solver.coinChange(coins, amount) == expected

def test_6():
    coins = [3, 5]
    amount = 11
    expected = 3
    assert solver.coinChange(coins, amount) == expected

