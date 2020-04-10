# Learning
# used nice graphical analysis to find the DP solution
# 


# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix) == 0:
            return 0

        MAX = 0
        dpMatrix = [[0]*(len(matrix[0])+1) for i in range((len(matrix)+1))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row = len(matrix)-i-1
                col = len(matrix[0])-j-1

                if matrix[row][col] == '0':
                    dpMatrix[row][col] = 0
                else:
                    dpMatrix[row][col] = 1 + min(dpMatrix[row+1][col], dpMatrix[row+1][col+1], dpMatrix[row][col+1])
                    if MAX < dpMatrix[row][col]:
                        MAX = dpMatrix[row][col]

        # print dpMatrix[0]
        # print dpMatrix[1]
        # print dpMatrix[2]
        # print dpMatrix[3]
        # print dpMatrix[4]

        return MAX*MAX

obj = Solution()
# print obj.maximalSquare([
#     [1, 0, 1, 0, 0],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0]
# ]
# )

print obj.maximalSquare([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
])