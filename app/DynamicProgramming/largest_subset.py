"""
DP: Largest Subset

In a scheduling system, there are n events represented by two arrays:
* start[i]: start time
* finish[i]: end time

A subset of events is considered high-priority if:
> There exists at least one event in the subset that overlaps (intersects) with every other event in the subset.

Overlap Rule:
Two events [a, b] and [c, d] overlap if:
* They share any time, including endpoints
* i.e., max(a, c) ≤ min(b, d)

Task
Determine:
> The maximum size of such a high-priority subset.

Notes
* Events touching at start/end are considered overlapping
* Multiple events may have identical times

Example
n = 4
start  = [1, 2, 3, 4]
finish = [2, 3, 5, 5]

Largest subset: [2,3], [3,5], [4,5]
Event [3,5] overlaps with all others → valid subset
Output: 3


"""
import bisect
from typing import List

class Solution:

    def getSubsetLength(self, start: List[int], finish: List[int]) -> int:
        starts = sorted(start)
        ends = sorted(finish)

        res = 0
        for s, f in zip(start, finish):
            # number of events that have finished before this event starts
            events_end_before_this = bisect.bisect_left(ends, s)

            # number of events that have started before this event finishes
            events_start_before_this = bisect.bisect_right(starts, f)

            # overlap = number of events that have started before this event finishes
            #           - number of events that have finished before this event starts
            overlap = events_start_before_this - events_end_before_this

            print(f"[s:{s}, f:{f}] -> {events_start_before_this} - {events_start_before_this} = {overlap}")
            res = max(res, overlap)

        print(f"res = {res}")
        return res

    def getSubsetLength2(self, start: List[int], finish: List[int]) -> int:
        n = len(start)
        res = 0

        for i in range(n):
            count = 0
            for j in range(n):
                if not (finish[j] < start[i] or start[j] > finish[i]):
                    count += 1
            res = max(res, count)

        return res
