"""
994. Rotting Oranges
Medium
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
Output: 4

Example 2:
Input: grid = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens
4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes_passed = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Initialize the queue with the positions of all rotten oranges and count the fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # If the cell contains a rotten orange, add its position to the queue
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    # If the cell contains a fresh orange, increment the fresh_count
                    fresh_count += 1

        # Infect the adjacent fresh oranges using BFS **************************
        # While there are rotten oranges to process and there are still fresh oranges
        while queue and fresh_count > 0:
            minutes_passed += 1 # Increment the minutes passed for each level of BFS
            # Process all the rotten oranges that are currently in the queue
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft() # popleft() removes a element from the left (front) of a queue
                for dx, dy in directions:   # Check all four directions (right, left, down, up)
                    nx, ny = x + dx, y + dy # Calculate the new position of the adjacent cell

                    # Check if the adjacent cell is within bounds and contains a fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2        # Mark the fresh orange as rotten
                        fresh_count -= 1        # Decrement the count of fresh oranges
                        queue.append((nx, ny))  # Add the newly rotten orange's position to the queue for the next round of BFS

        # If there are no fresh oranges left, return the minutes passed; otherwise, return -1
        return minutes_passed if fresh_count == 0 else -1
