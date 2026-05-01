import pytest

from app.DynamicProgramming.meeting_rooms_252 import Solution

solver = Solution()

def test_1():
    assert solver.canAttendMeetings([[0,30],[5,10],[15,20]]) == False

def test_2():
    assert solver.canAttendMeetings([[0,30],[35,50]]) == True



        