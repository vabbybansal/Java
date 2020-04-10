# AMAZING using two pointer again
# Learning
# If it had asked for all index values, this would have been a n^3 algorithm, since k pointer would travel back till j each time condition gets satisfied (see commented code)
# since it only asks for total triplets, we do not need k to go back, and can calculate all number if pairs with k on its place

# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# Example:
#
# Input: nums = [-2,0,1,3], and target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sortedIndices = sorted(range(len(nums)), key=lambda k: nums[k])
        sortedArr = [0]*len(nums)
        for i in range(len(nums)):
            sortedArr[i] = nums[sortedIndices[i]]

        totals = 0

        for i in range(len(nums)-2):

            j = i+1
            k = len(nums)-1
            jkMax = target - sortedArr[i]

            while j < k:

                if sortedArr[j] + sortedArr[k] >= jkMax:
                    k -= 1
                else:

                    # grab all
                    # temp = k
                    # while temp > j:
                    #     totals += 1
                    #     temp -= 1
                    # j += 1


                    totals += (k-j)

                    j += 1

        return totals

print Solution().threeSumSmaller(nums = [-2,0,1,3], target = 2)
print Solution().threeSumSmaller(nums = [-2,0,1,3,5], target = 2)
print Solution().threeSumSmaller(nums = [-2,0,1,3,5], target = 3)
print Solution().threeSumSmaller(nums = [-2,0,1,3,5], target = -99)