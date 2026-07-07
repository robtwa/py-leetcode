import pytest

from app.DynamicProgramming.meeting_rooms_ii_253 import Solution

solver = Solution()

def test_1():
    assert solver.minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    



        