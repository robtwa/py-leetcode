"""
Meeting Rooms (LC 252)
Easy

You are given an array of meeting time intervals, where each interval is represented as intervals[i] = [start_i, end_i].
Each interval contains a start time and an end time for a meeting.
Your task is to determine whether a person can attend all the meetings without any time conflicts.

A person can attend all meetings if no two meetings overlap in time.
Two meetings overlap if one meeting starts before the other meeting ends.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation:
The meeting [0,30] overlaps with [5,10], so it is not possible to attend all meetings.

Example 2:
Input: intervals = [[0,30],[35,50]]
Output: true
Explanation:
These don't overlap because the second meeting starts after the first one ends. The person can attend both meetings.
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort() # sort by start time
        n = len(intervals)

        for i in range(n - 1):
            curr_interval = intervals[i]
            next_interval = intervals[i+1]

            if next_interval[0] <= curr_interval[1]:
                return False

        return True



