# Learnings
# Two finger algorithm

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
#
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # [-9,-5,1,4,6,8]
        # [1,16,25,36,64,81]
        # o(n) + o(nlogn)


        # [25,81]
        # [1, 16, 36, 64]

        # Binary search: O(logn) or traversal to find first positive: O(n)
        # Create squared lists: O(n) :
        #   inplace or out of place
        #         inplace: put squares in same array
        # Two finger algorithm: O(n)
        # Possible optmizations..
        # o(n)

        # Test Cases
        # All negative
        # All positive
        # Mixture
        # Empty
        # Multiple duplicate numbers especially zeros / first positive number

        out = [0]*len(A)
        found = False
        # Find first positive number
        for i in range(len(A)):
            if A[i] >= 0:
                found = True
                break
        firstPosInd = i
        if not found:
            firstPosInd += 1

        # Inplace squares with same sequence
        for i in range(len(A)):
            A[i] = A[i]*A[i]

        # Two finger with negative array in negative order
        negArrInd = firstPosInd - 1  #[check overflow]
        posArrInd = firstPosInd

        outInd = 0
        while outInd < len(A):

            if posArrInd >= len(A) or A[posArrInd] >= A[negArrInd]:
                out[outInd] = A[negArrInd]
                negArrInd -= 1

            elif negArrInd <= -1 or A[posArrInd] < A[negArrInd]:
                out[outInd] = A[posArrInd]
                posArrInd += 1
            outInd += 1

        return out


print Solution().sortedSquares([-10,-1,1,2,3])


    # def binarySearchHandler(self, A, target):
    #
    #     # Find the first positive number
    #     return self.almostBinarySearch(A, target, 0, len(A))
    #
    # def almostBinarySearch(A, target, i, j):
    #
    #     # Base
    #     if j-i+1 == 1:
    #         pass
    #
    #     centerInd = (i+j)/2
    #
    #     if target == A[centerInd]:
    #         # could be possible
