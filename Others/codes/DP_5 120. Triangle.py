# DP

# Learnings:
# Format decided in DP_4 was good
# Additional learning: always store left in left and right in right vairables and do not do operation min/sum directly
# ANOTHER MAJOR LEARNING ABOUT RECURSION: within a recursion fun abc, do not do paths = paths + abc(left) .... This is my natural tendency but doesnt work well
    # Rather, do
#       left = abc(left),
#       right = abc(right)
#       The above variables give output from those nodes | Consider this as values which get calculated in a node and get passed around to the others
#       Now, in a separate line, do whatever operations needs to be done
#       Example of operations:
#             1) find sum: node_sum = left + right + this_node
#             2) find min: node_val = min(left, right) + this_node

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#     [2],
#     [3,4],
#     [6,5,7],
#     [4,1,8,3]
# ]

class Solution(object):

    def minimumTotal(self, triangle):
        levels = len(triangle)
        MEM = {}

        def go_below(i, j):

            # Create hash key for node
            hash_key = str(i) + '_' + str(j)

            # Check if node value already stored in the DP dict
            if hash_key in MEM:
                return MEM[hash_key]

            # Check feasibility - NODE ALWAYS FEASIBLE [goes either to left or to right within base case, so never overruns]

            # Check base/leaf case
            if i == levels - 1:
                return triangle[i][j]

            # Navigate below
            left = go_below(i+1, j)
            right = go_below(i+1, j+1)

            # Value for this node
            MEM[hash_key] = min(left, right) + triangle[i][j]

            return MEM[hash_key]

        # Start the seed
        return go_below(0, 0)

obj = Solution()
print obj.minimumTotal([
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
])

