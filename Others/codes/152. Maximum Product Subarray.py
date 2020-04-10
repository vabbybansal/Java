# DP

class Solution(object):
    def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_MAX = nums[0]
        prev_MIN = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            curr_MAX = max(curr, curr*prev_MAX, curr*prev_MIN)
            curr_MIN = min(curr, curr*prev_MAX, curr*prev_MIN)

            ans = max(curr_MAX, ans)

            prev_MAX = curr_MAX
            prev_MIN = curr_MIN

        return ans


# Idea: Maximum product of subarray of the full array is the same as 'aggregated' over multiple sub-problems
# The best that I can do at index i is either elem at index i, or the best till the previous index with addition of the elem at i
# That is - this item, or continue the max subarray from prev item
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prev_MAX = nums[0]
    prev_MIN = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        curr_MAX = max(curr, curr*prev_MAX, curr*prev_MIN)
        curr_MIN = min(curr, curr*prev_MAX, curr*prev_MIN)

        prev_MAX = curr_MAX
        prev_MIN = curr_MIN

    return curr_MAX

print maxProduct([2,3,-2,4])


# def maxProduct(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     mem = dict()
#     mem['MAX'] = nums[0]
#
#     def f(i,j):
#         key = str(i)+'_'+str(j)
#         if key in mem:
#             return mem[key]
#         if i == j:
#             store(key, nums[i])
#             return nums[i]
#
#
#         # Send calculation for left side which will not be used but needs to be computed
#         f(i, j-1)
#
#         right_this = f(i+1, j) * nums[i]
#
#         # Store this sequence product
#         store(str(i)+'_'+str(j), right_this)
#
#         return right_this
#
#
#     def store(key, val):
#         if key in mem:
#             return mem[key]
#         else:
#             mem[key] = val
#
#             if mem['MAX'] < val:
#                 mem['MAX'] = val
#
#     f(0, (len(nums)-1))
#     return mem['MAX']
#
# print maxProduct([2,3,-2,4])