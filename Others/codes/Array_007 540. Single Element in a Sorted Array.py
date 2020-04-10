# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
#
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: [3,3,7,7,10,11,11]
# Output: 10


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # [1,1,2,2,3,3,6,6,8,10,10]
        # = 8

        # ideal scenario: first element always has even index (starts with 0)
        # all pairs AFTER the flawed element will have first element at odd


        # Binary Search
        # Loop
        #   Middle
        #       Find left and right. Find pair. Check for left of pair
        #       Also check for this element
        #           If even: go right
        #           If odd: go left

        return self.binarySearchSingleNonDuplicate(nums, 0, len(nums)-1)

    def binarySearchSingleNonDuplicate(self, myArray, i, j):


        if i == j: ## CHECK THIS
            return myArray[i]

        centerElmInd = (i+j)/2
        centerElm = myArray[centerElmInd]

        # leftElmInd =
        # rightElmInd = centerElmInd + 1

        # Edge cases: center elm = first elm / last elm
        if centerElmInd - 1 < 0: return centerElm
        if centerElmInd + 1 >= len(myArray): return centerElm

        # center element itself is the lone wolf
        if myArray[centerElmInd] != myArray[centerElmInd+1] and myArray[centerElmInd] != myArray[centerElmInd-1]:
            return myArray[centerElmInd]

        # not equal to element on the right: left elem is the starting elm
        else:
            if myArray[centerElmInd] != myArray[centerElmInd+1]:
                leftElmInd = centerElmInd-1
            else:
                leftElmInd = centerElmInd

            if (leftElmInd)%2 == 0:
                # violatation on the right
                return self.binarySearchSingleNonDuplicate(myArray, leftElmInd + 2, j)
            else:
                return self.binarySearchSingleNonDuplicate(myArray, i, leftElmInd-1)

            # else:
            #     # rightElm = myArray[centerElmInd-1]
            #     # violation on the left
            #     return self.binarySearchSingleNonDuplicate(myArray, i, centerElmInd-1)

        #     if (centerElmInd-1)%2 == 0:
        #         # violatation on the right
        #         return self.binarySearchSingleNonDuplicate(myArray, centerElmInd + 1, j)
        #     else: return self.binarySearchSingleNonDuplicate(myArray, i, centerElmInd-1)
        #
        # else:
        #     # rightElm = myArray[centerElmInd-1]
        #     # violation on the left
        #     return self.binarySearchSingleNonDuplicate(myArray, i, centerElmInd-1)



# [1,1,6,6,8,10,10]
# [0,1,2,3,4, 5, 6]

print Solution().singleNonDuplicate([1,1,6,6,8,8,10])
print Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print Solution().singleNonDuplicate([1,1,2,2,3])
