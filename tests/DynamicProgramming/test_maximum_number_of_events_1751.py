from app.DynamicProgramming.maximum_number_of_events_1751 import Solution

solver = Solution()

def test_1():
    events = [[1,2,4],[3,4,3],[2,3,1]]
    k = 2
    expected = 7

    result = solver.maxValue(events, k)

    assert result == expected

def test_2():
    events = [[1,2,4],[3,4,3],[2,3,10]]
    k = 2
    expected = 10

    result = solver.maxValue(events, k)

    assert result == expected

def test_3():
    events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    k = 3
    expected = 9

    result = solver.maxValue(events, k)

    assert result == expected
