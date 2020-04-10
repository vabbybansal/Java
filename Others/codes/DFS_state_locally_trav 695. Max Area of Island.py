# Learning
# 1) Baking it further - varible sum in recursion function passed over locally, no global class variable used
# 2) used constant space by changing the input - marking visited node as -1

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        areaCurrentMax = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                area = self.startDFS(row, col, grid, 0)
                if area > areaCurrentMax:
                    areaCurrentMax = area
        return  areaCurrentMax

    def startDFS(self, row, col, grid, currentSum):
        # Check for validity
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return currentSum

        # check if visited
        if grid[row][col] == -1 or grid[row][col] == 0:
            return currentSum

        # Mark visited
        grid[row][col] = -1

        # increment sum
        currentSum += 1

        # Traverse in all directions
        currentSum = self.startDFS(row+1, col, grid, currentSum)
        currentSum = self.startDFS(row-1, col, grid, currentSum)
        currentSum = self.startDFS(row, col+1, grid, currentSum)
        currentSum = self.startDFS(row, col-1, grid, currentSum)

        return currentSum

obj = Solution()
print obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                           [0,0,0,0,0,0,0,1,1,1,0,0,0],
                           [0,1,1,0,1,0,0,0,0,0,0,0,0],
                           [0,1,0,0,1,1,0,0,1,0,1,0,0],
                           [0,1,0,0,1,1,0,0,1,1,1,0,0],
                           [0,0,0,0,0,0,0,0,0,0,1,0,0],
                           [0,0,0,0,0,0,0,1,1,1,0,0,0],
                           [0,0,0,0,0,0,0,1,1,0,0,0,0]])
print obj.maxAreaOfIsland([[0,0,0,0,0,0,0,0]])