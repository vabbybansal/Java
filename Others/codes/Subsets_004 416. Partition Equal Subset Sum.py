# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        sum = 0
        for num in nums:
            sum += num
        if sum %2 == 1:
            return False
        self.DP_FailSets = set()
        return True if self.addNumberToSets(0,0,0) else False

    def addNumberToSets(self, l, r, ind):

        if l <= r:
            if (l,ind) in self.DP_FailSets:
                return False
        else:
            if (r,ind) in self.DP_FailSets:
                return False


        # if (l,r,ind) in self.DP_FailSets:
        #     return False

        if ind == len(self.nums):
            if l == r:
                return True
            else:
                return False

        # Add the index number to left set
        left = self.addNumberToSets(l+self.nums[ind],r,ind+1)
        if left:
            return True

        # Else, try adding the number to the other set
        right = self.addNumberToSets(l,r+self.nums[ind],ind+1)
        if right:
            return True

        # Code reaches here - current comb not possible
        if l <= r:
            self.DP_FailSets.add((l, ind))
        else:
            self.DP_FailSets.add((r, ind))

obj = Solution()
# print obj.canPartition([1, 5, 11, 5])
# print obj.canPartition([1, 2, 3, 5])
# print obj.canPartition([])
print obj.canPartition([1,2])