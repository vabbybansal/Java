# LEARNINGS
# Can be done using hash table
# Another cool method is using two pointers on a sorted array which also gives O(n), but much more cleaner

# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# Example:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# Using hash table - O(n)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        freqDict = dict()
        # Put element freq
        for i in range(len(numbers)):
            elm = numbers[i]
            if elm not in freqDict:
                freqDict[elm] = {'freq':0, 'index':[]}
            freqDict[elm]['freq'] += 1
            freqDict[elm]['index'].append(i)

        # Pass over once and check if reqd has a freq in the leftover elems
        for i in range(len(numbers)):
            elm = numbers[i]
            freqDict[elm]['freq'] -= 1

            reqd = target-elm
            if reqd in freqDict and freqDict[reqd]['freq'] > 0:
                ind2 = freqDict[reqd]['index'][0]
                if ind2 == i:
                    ind2 = freqDict[reqd]['index'][1]
                mini = min(i, ind2)
                maxi = max(i, ind2)
                return [mini+1, maxi+1]
            freqDict[elm]['freq'] += 1


# Using two pointers - O(n) (uses the sorted property)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        while i < j:

            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1,j+1]


obj = Solution()
print obj.twoSum(numbers = [2,7,11,15], target = 9)
print obj.twoSum(numbers = [2,7,2,11,15,2], target = 4)