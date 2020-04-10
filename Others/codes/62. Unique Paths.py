# DP

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    path_memory = dict()

    def traverse_to(i, j, num_paths, path_memory):

        # Use DP to check if contrib / num_paths are already calculated
        memory_node_key = str(i)+'_'+str(j)
        if memory_node_key in path_memory:
            return num_paths + path_memory[memory_node_key]

        prv_num_paths = num_paths

        # Base
        if (i == m-1) & (j == n-1):
            num_paths += 1
            return num_paths
        elif((i > m-1) or (j > n-1)):
            return num_paths

        # go Down
        num_paths = traverse_to(i, j+1, num_paths, path_memory)

        # go Right
        num_paths = traverse_to(i+1, j, num_paths, path_memory)

        gain_in_num_paths = num_paths - prv_num_paths
        # Store the gain (this node's contribution to memory for future use (DP))
        # Given the fact that once for a node both down and right are complete, we know its absolute contrib / num_paths to target
        path_memory[memory_node_key] = gain_in_num_paths

        return num_paths

    num_paths = traverse_to(0,0,0, path_memory)
    return num_paths

print uniquePaths(3, 2)




# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# #
# # The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# #
# # Now consider if some obstacles are added to the grids. How many unique paths would there be?
# #
# #
# #
# # An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# #
# # Note: m and n will be at most 100.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        if obstacleGrid[0][0] == 1:
            return 0

        rows = m = len(obstacleGrid)
        cols = n = len(obstacleGrid[0])
        path_memory = dict()

        def traverse_to(i, j, num_paths, path_memory):

            # Use DP to check if contrib / num_paths are already calculated
            memory_node_key = str(i)+'_'+str(j)
            if memory_node_key in path_memory:
                return num_paths + path_memory[memory_node_key]

            prv_num_paths = num_paths

            # Base
            if (i == m-1) & (j == n-1):
                num_paths += 1
                return num_paths
            elif((i > m-1) or (j > n-1)):
                return num_paths

            # go Right
            if j+1 <= n-1:
                if obstacleGrid[i][j+1] != 1:
                    num_paths = traverse_to(i, j+1, num_paths, path_memory)

            # go Down
            if i+1 <= m-1:
                if obstacleGrid[i+1][j] != 1:
                    num_paths = traverse_to(i+1, j, num_paths, path_memory)

            gain_in_num_paths = num_paths - prv_num_paths
            # Store the gain (this node's contribution to memory for future use (DP))
            # Given the fact that once for a node both down and right are complete, we know its absolute contrib / num_paths to target
            path_memory[memory_node_key] = gain_in_num_paths

            return num_paths

        num_paths = traverse_to(0,0,0, path_memory)
        return num_paths