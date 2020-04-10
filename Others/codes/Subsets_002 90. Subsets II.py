# Learnings
# For this, I had to use some sort of set to make sure dupes are not added
# For that, could create string representation of a set bby running a for-loop from first to last membber every time. Rather used DP there to use the last set string and append the new char into it using recursive DFS

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
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        # sort the list
        nums.sort()
        DPSet = set()

        allSubSets = [[]]
        # self.DFS(0, [], allSubSets, nums)
        self.DFS_Dup(0, [], allSubSets, DPSet, "", nums)
        return allSubSets

    def DFS(self, elmNum, subSet, allSubsets, nums):

        if elmNum >= len(nums):
            return

        elm = nums[elmNum]
        newSubSet = subSet + [elm]
        allSubsets.append(newSubSet)

        self.DFS(elmNum+1, subSet, allSubsets, nums)
        self.DFS(elmNum+1, newSubSet, allSubsets, nums)

    def DFS_Dup(self, elmNum, subSet, allSubsets, DPSet, hashString, nums):

        if elmNum >= len(nums):
            return

        elm = nums[elmNum]
        newHashString = hashString + '_' + str(elm)
        if newHashString in DPSet:
            # Do Nothing
            i = 1
        else:
            DPSet.add(newHashString)
            newSubSet = subSet + [elm]
            allSubsets.append(newSubSet)
            self.DFS_Dup(elmNum+1, newSubSet, allSubsets, DPSet, newHashString, nums)

        self.DFS_Dup(elmNum+1, subSet, allSubsets, DPSet, hashString, nums)




obj = Solution()
# print obj.subsetsWithDup(nums = [1,2,2])
# print obj.subsetsWithDup(nums = [])
# print obj.subsetsWithDup(nums = [1])
print obj.subsetsWithDup([1,1,2,2])