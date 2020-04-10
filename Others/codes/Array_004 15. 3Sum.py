# Learning
# Instead of iterating on pairs od array elms, instead iterate on hash keys rather for faster soln

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        freqDict = {}
        self.tripletSet = set()
        self.dedupedTriplets = []

        for num in nums:
            if num not in freqDict:
                freqDict[num] = 0
            freqDict[num] += 1

        for i in freqDict.keys():
            freqDict[i] -= 1
            for j in freqDict.keys():
                if freqDict[j] >= 1:
                    freqDict[j] -= 1

                    reqdNum = -(i+j)
                    if reqdNum in freqDict and freqDict[reqdNum]>=1:
                        self.storeTriplet(i, j, reqdNum)
                    freqDict[j] += 1
            freqDict[i] += 1

        return self.dedupedTriplets

    def storeTriplet(self, a, b, c):
        minT = min(a,b,c)
        maxT = max(a,b,c)

        if (minT, maxT) not in self.tripletSet:
            self.tripletSet.add((minT, maxT))
            self.dedupedTriplets.append([a,b,c])

obj = Solution()
print obj.threeSum([-1, 0, 1, 2, -1, -4])