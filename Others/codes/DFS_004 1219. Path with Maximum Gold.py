# Very Important learning:
# if we remove nodes from visited set at the end of a node's DFS call (at the very end after all navigations to left right bottom up), then we essentially explore all paths using DFS, which was required here



# In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
#
# Return the maximum amount of gold you can collect under the conditions:
#
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
#
#
# Example 1:
#
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# Example 2:
#
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if grid == []:
            return 0

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.maxPath = 0
        self.memoryVisit = set()

        for i in range(self.rows):
            for j in range(self.cols):
                # self.memoryVisit = set()
                self.DFS(i, j, 0)

        return self.maxPath

    def getCellKey(self, i, j):
        return (2**i) * (3**j)



    def DFS(self, i, j, pathSum):

        # Feasibility
        if i >= self.rows or j >= self.cols or i < 0 or j < 0:
            return

        # Check if already visited
        cellKey = self.getCellKey(i,j)
        if cellKey in self.memoryVisit:
            return
        else:
            # Mark visited
            self.memoryVisit.add(cellKey)

        if self.grid[i][j] == 0:
            return

        pathSum += self.grid[i][j]
        if pathSum > self.maxPath:
            self.maxPath = pathSum

        # Nav right left bottom up
        # Right
        self.DFS(i, j+1, pathSum)
        # Bottom
        self.DFS(i+1, j, pathSum)
        # Left
        self.DFS(i, j-1, pathSum)
        # Up
        self.DFS(i-1, j, pathSum)

        self.memoryVisit.remove(cellKey)

obj = Solution()
# print obj.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])

print obj.getMaximumGold([
    [0,  0,  19, 5, 8],
    [11, 20, 14, 1, 0],
    [0,  0,  1,  1, 1],
    [0,  2,  0,  2, 0]
]
)