# Learnings
# Struggled very much
# if I am trying to iterate an array in a usual way with two pointers, that will not give a soln. it takes O(n2) time but there are 2^n subsets possubble
# All subsets => traversing all in a graph. for each number, we push the current subsets and current subsets with the additional number
# Viz: https://docs.google.com/document/d/1TG96Ae8EYGDq-Uz-OM7wGBr1i3oTTBR2zJGZ7tnHqMc/edit?folder=1sSaIdBp85lxaDv6HL6_kKmQW-F6XTD9t

# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#     [3],
#     [1],
#     [2],
#     [1,2,3],
#     [1,3],
#     [2,3],
#     [1,2],
#     []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]


        allSubSets = [[]]
        for elm in nums:
            lenSubSets = len(allSubSets)
            for i in range(lenSubSets):
                subSet = allSubSets[i]
                allSubSets.append(subSet + [elm])
        return allSubSets

obj = Solution()
print obj.subsets(nums = [1,2,3])
print obj.subsets(nums = [])
print obj.subsets(nums = [1])