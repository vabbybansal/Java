# DFS
# SOL: The idea is that we keep moving along the island till the island boundaries, and return just one walk / 1 for the whole island, and sum up all such walks


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])

        walked = [ ([0] * cols) for row in range(rows) ]
        numIslands = 0

        def randomWalk(i, j):


            # Validate i and j
            if i < 0 or i > (rows-1) or j<0 or j > (cols-1):
                return 0

            # If already walked, then don't care
            if walked[i][j] == 1:
                return 0

            # Mark as walked so that the cell is not visited again
            walked[i][j] = 1

            # If cell value is 0, do not navigate further and return 0
            if grid[i][j] == "0":
                return 0

            # if cell value is 1, it means that the island is continuing. Walk further right, down, left and bottom
            randomWalk(i, j+1)
            randomWalk(i+1, j)
            randomWalk(i, j-1)
            randomWalk(i-1, j)

            # If the code reaches here, it means that some island has been nevigated completely. Return 1
            return 1

        # Navigate all the island cells. Many of them will be already visited recursively and return will be 0
        for i in range(rows):
            for j in range(cols):
                numIslands += randomWalk(i, j)


        return numIslands


obj = Solution()
print obj.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]]
)