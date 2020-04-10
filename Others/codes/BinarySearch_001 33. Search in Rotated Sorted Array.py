# Learnings
# Struggeled with the iterative nature of logic
# There was no underlying 'logic' intiutive theme - more of what happens if pivot > target and violation is on left side...
# Just try to write down on whiteboard all cases and try to condense them into an underlying logic for cleaner code
# https://docs.google.com/document/d/13VamVpdH4WJi6eqA1m1PQ5ScoI-Ub03Nw6SZfGCP3a8/edit?folder=1sSaIdBp85lxaDv6HL6_kKmQW-F6XTD9t

# Anothe way coud have been - find pivot element and then choose the array to go to (two pass though)

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        return self.binarySearchWithViolation(nums, 0, len(nums)-1, target)

    def binarySearchWithViolation(self, array, start, end, target):

        if start == end:
            if target == array[start]:
                return start
            else: return -1

        if start == end-1:
            if target == array[start]:
                return start
            elif target == array[start+1]:
                return start+1
            else: return -1

        pivot = start + (end-start)/2
        idealSide = 1 if target > array[pivot] else 0

        # # Check violation side
        if array[pivot] < array[start]:
            # Violation on the left
            violationSide = 0
        elif array[pivot] > array[end]:
            # Violation on the right
            violationSide = 1
        else:
            # No violation
            return self.binarySearch(array, start, end, target)

        if violationSide == idealSide:
            # go violation side
            if violationSide == 0: # go left
                return self.binarySearchWithViolation(array, start, pivot, target)
            else:
                return self.binarySearchWithViolation(array, pivot, end, target)
        else:
            if target >= array[start]:
                # go left
                return self.binarySearchWithViolation(array, start, pivot, target)
            else:
                # go right
                return self.binarySearchWithViolation(array, pivot, end, target)

    def binarySearch(self, array, start, end, target):

        if start == end:
            if target == array[start]:
                return start
            else: return -1

        pivot = start + (end-start)/2

        if target <= array[pivot]:
            newStart = start
            newEnd = pivot

        else:
            newStart = pivot+1
            newEnd = end

        return self.binarySearch(array, newStart, newEnd, target)

obj = Solution()
print obj.search([1,2,3,4,5,6], 5)
print obj.search([4,5,6,1,2,3], 5)
print obj.search([4,5,6,1,2,3], 6)
print obj.search([4,5,6,1,2,3], 2)

print obj.search([4,5,6,7,8,3], 3)
print obj.search([4,5,6,7,8,3], 5)