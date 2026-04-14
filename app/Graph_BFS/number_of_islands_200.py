"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List

class Solution:
    # This function counts the number of islands in a 2D grid.
    # '1' represents land and '0' represents water.
    # It uses BFS (Breadth-First Search):
    # Whenever a '1' is found, BFS is triggered to mark all connected land
    # (up, down, left, right) as '0' (visited).
    # Each BFS call represents discovering one island.
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = [(r, c)] # Initialize the queue with the starting cell
            while queue: # While there are cells to process
                x, y = queue.pop(0) # Pop the first cell from the head of the queue

                # Check if the cell is within bounds and is land ('1')
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                    grid[x][y] = '0'  # Mark as visited
                    queue.append((x + 1, y))
                    queue.append((x - 1, y))
                    queue.append((x, y + 1))
                    queue.append((x, y - 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    # Call BFS to mark all connected land as visited
                    bfs(i, j)

        return count