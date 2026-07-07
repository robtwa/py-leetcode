"""
253. Meeting Rooms II
Medium

Problem Description
You are given an array of meeting time intervals where each interval is represented as intervals[i] = [start_i, end_i].
Each interval indicates when a meeting starts and ends.

Your task is to find the minimum number of conference rooms required to schedule all the meetings without any conflicts.
In other words, if two or more meetings overlap in time, they need separate conference rooms.

For example, if you have meetings [[0,30],[5,10],[15,20]], the first meeting runs from time 0 to 30.
The second meeting (5 to 10) overlaps with the first, so you need a second room.
The third meeting (15 to 20) also overlaps with the first, but since the second meeting has already ended by time 15,
you can reuse that room.
Therefore, you need a minimum of 2 conference rooms.

The solution uses a difference array technique.
It tracks the changes in the number of ongoing meetings at each time point.
By marking +1 when a meeting starts and -1 when it ends, then calculating the running sum, you can determine the maximum
number of simultaneous meetings at any point in time, which equals the minimum number of rooms needed.


"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort() # sort by start time

        # min-heap of end times
        min_heap_end = []

        for start, end in intervals:
            # if the earliest ending meeting has ended before the current meeting starts, we can reuse that room
            if min_heap_end and min_heap_end[0] <= start:
                heapq.heappop(min_heap_end) # remove the meeting that has ended

            # add the current meeting's end time to the heap
            heapq.heappush(min_heap_end, end)

        return len(min_heap_end)

