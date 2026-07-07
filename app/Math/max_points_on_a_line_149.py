"""
149. Max Points on a Line
Hard

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of
points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # if ≤ 2 points, all are collinear
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)  # slope frequency map
            dup = 1  #  duplicates (including self)
            local_max = 0

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # handle duplicate points
                if x1 == x2 and y1 == y2:
                    dup += 1
                    continue

                dy = y2 - y1
                dx = x2 - x1

                # reduce to simplest fraction via gcd
                g = self.gcd(abs(dy), abs(dx))
                if g != 0:
                    dy //= g
                    dx //= g

                # normalize sign to make representation unique
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1  #  vertical line
                elif dy == 0:
                    dx = 1  #  horizontal line

                key = (dy, dx)
                slopes[key] += 1

                # update local maximum count
                local_max = max(local_max, slopes[key])

            # max points on a line through this anchor
            ans = max(ans, local_max + dup)

        return ans

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

