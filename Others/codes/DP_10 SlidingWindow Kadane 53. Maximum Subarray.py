# Learnings
# Kadane's algorithm
# http://theoryofprogramming.com/2016/10/21/dynamic-programming-kadanes-algorithm/

# How I converted suboptimal O(n^2) to O(2^n)
# https://docs.google.com/document/d/1aACr9Aztz5dfMyhow0UAFuMRujVMGjWu-uY-mpRcwxM/edit


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        globalMax = nums[0]
        localMaxEndingAtLastIndex = nums[0]

        for i in range(1,len(nums)):
            nextElm = nums[i]

            localMaxEndingAtIndex = max(nextElm, nextElm + localMaxEndingAtLastIndex)

            if localMaxEndingAtIndex > globalMax:
                globalMax = localMaxEndingAtIndex
            localMaxEndingAtLastIndex = localMaxEndingAtIndex
        return globalMax

obj = Solution()
print obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])