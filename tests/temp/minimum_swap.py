from app.temp.minimum_swap import Solution

solver = Solution()

def test1():
    assert solver.minimumSwap([1,0,1,0]) == 1

def test2():
    assert solver.minimumSwap([1,0,0,1,0]) == 2
