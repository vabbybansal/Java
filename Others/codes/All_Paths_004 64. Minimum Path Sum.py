# Learning
# [Bottom-up with O(n) space and immutabble input matrix]
# if I do a bottom up, then i can start from last row and go up (or last column and go left). Using that, I can reduce extra dict space to store only the kast row / col at a time which would bbe v nice
# This is beautifully done in the soln '# Bottom-Up with immutable original matrix' Please check it out
# [Bottom-up with mutable matrix and O(1) space]
# one step further, i can place the calc values onto the matrix itself and it would become without extra space

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# #
# # Note: You can only move either down or right at any point in time.
# #
# # Example:
# #
# # Input:
# # [
# #     [1,3,1],
# #     [1,5,1],
# #     [4,2,1]
# # ]
# # Output: 7


# Top Down
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.grid = grid
        self.MEM = {}

        if len(grid) == 0:
            return float('inf')

        return self.minSumFromIJ(0,0)

    def minSumFromIJ(self, i, j):

        # Check Validity
        if i >= len(self.grid) or i < 0 or j >= len(self.grid[0]) or j < 0:
            return float('inf')

        if (i,j) in self.MEM: return self.MEM[(i,j)]

        # Base Case
        if i == len(self.grid)-1 and j == len(self.grid[0])-1: return self.grid[i][j]

        # Navigate
        self.MEM[(i,j)] = self.grid[i][j] + min(self.minSumFromIJ(i+1,j), self.minSumFromIJ(i,j+1))

        return self.MEM[(i,j)]

# Optimized Bottom-Up
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if i == len(grid)-1 and j == len(grid[0])-1:
                    continue
                elif i == len(grid)-1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                elif j == len(grid[0])-1:
                    grid[i][j] = grid[i][j] + grid[i+1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])


        return grid[0][0]

# Bottom-Up with immutable original matrix
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dp_row = [float('inf')]*len(grid[0])
        dp_row[len(grid[0])-1] = 0

        for i in range(len(grid)-1, -1, -1):

            dp_row[len(grid[0])-1] += grid[i][len(grid[0])-1]

            for j in range(len(grid[0])-1-1, -1, -1):

                dp_row[j] = grid[i][j] + min(dp_row[j], dp_row[j+1])



        return dp_row[0]


print Solution().minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
])