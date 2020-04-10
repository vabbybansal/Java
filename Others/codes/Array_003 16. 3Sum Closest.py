# Learnings
# Similar to 3sum but cant use hash table as hashh table not good for 'approximates', rather good for equals
# This neat two pointer thing is very cool and is similar to twoSum using no hash table and also, its really good with approximates and finds two sum in O(n)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


# Way to think
# Sol 1
#   Look at all triplets - O(n^3)
# Sol 2
#   sort O(nlogn)
#   for each elm i O(n)
#       two pointer search for closest pair O(n)
# -------
#   Total: O(nlogn) + O(n^2) => O(n^2)



# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # sort the array to be able to run the two pointer logic
        nums.sort()

        minDiff = float('inf')
        outSum = 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            # for each i, put j next to i and k at the last and move j to right and k to left depending on how their sum fares with the required value
            while j < k:
                localSumReqd = target - nums[i]
                twoSum = nums[j] + nums[k]
                if minDiff > abs(target - nums[i] - twoSum):
                    minDiff = abs(target - nums[i] - twoSum)
                    outSum = nums[i] + twoSum

                if twoSum < localSumReqd:
                    j += 1
                elif twoSum > localSumReqd:
                    k -= 1
                else:
                    return target


        return outSum

out = Solution()
print out.threeSumClosest(nums = [-1, 2, 1, -4], target = 1)
print out.threeSumClosest(nums = [1,1,1], target = 1)
print out.threeSumClosest(nums = [-1, 2, 0,2,10], target = 1)