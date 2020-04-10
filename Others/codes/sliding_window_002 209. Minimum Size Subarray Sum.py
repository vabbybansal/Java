# Learning
# Done using two pointers, the forward exploratory pointer called expandPointer, backward one called compressPointer
# I was confused for a while as I was trying to force put in Kadane's algortihm (DP_10 Maximum Subarray)

#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        compressPointer = 0
        expandPointer = 0
        boundingSum = nums[0]
        MIN = 9999999999999

        while expandPointer < len(nums):
            if boundingSum >= s:

                # update min
                possibleMin = expandPointer - compressPointer + 1
                if possibleMin < MIN:
                    MIN = possibleMin
                # compress the compress pointer
                # if the back pointer is behind the forward pointer, push it more forward iteratively to see if we can remove some elements and still have a sum >= s
                if compressPointer < expandPointer:
                    boundingSum -= nums[compressPointer]
                    compressPointer += 1
                else:
                    expandPointer += 1
                    if expandPointer < len(nums):
                        boundingSum += nums[expandPointer]

            else:
                expandPointer += 1
                if expandPointer < len(nums):
                    boundingSum += nums[expandPointer]
        return MIN if MIN != 9999999999999 else 0

obj = Solution()
print obj.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3])
print obj.minSubArrayLen(s = 4, nums = [1,4,4])