# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
#
# If there is no non-empty subarray with sum at least K, return -1.
#
#
#
# Example 1:
#
# Input: A = [1], K = 1
# Output: 1
# Example 2:
#
# Input: A = [1,2], K = 4
# Output: -1
# Example 3:
#
# Input: A = [2,-1,2], K = 3
# Output: 3


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        self.A = A
        self.lenA = len(A)

        # Memorizes the fact that a certain path of (index, sum) has already been tried and tested, and prevents multiple such paths because of dupicicy
        self.DP_Set = set()

        # Variable to store the min
        self.MIN = 99999999999

        self.K = K

        # Initiate the recursion
        self.navigateAllPaths(0, 0, 0)

        if self.MIN < 99999999999:
            return self.MIN
        else:
            return -1

    def navigateAllPaths(self, index, sum, length):

        # DP check to see if a path of (index, sum) has already been initiated (no need to duplicate)
        if (index, sum) in self.DP_Set:
            return

        # Add to DP
        self.DP_Set.add((index, sum))

        # Check if the current length < self.MIN, GIVEN that all conditions and prereqs are satisfied
        if sum >= self.K and length < self.MIN:
            self.MIN = length

        # Base condition: Stop exploring paths once reached the last index element
        if index >= self.lenA:
            return

        # Navigate to other paths
        nextNum = self.A[index]
        # Nav to only next num
        self.navigateAllPaths(index+1, nextNum, 1)

        # Nav to current sum + next num
        self.navigateAllPaths(index+1, sum + nextNum, length+1)


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        self.A = A
        self.lenA = len(A)

        # Memorizes the fact that a certain path of (index, sum) has already been tried and tested, and prevents multiple such paths because of dupicicy
        self.DP_Set = set()

        # Variable to store the min
        self.MIN = 99999999999

        self.K = K

        # Initiate the recursion
        self.navigateAllPaths(0, 0, 0)

        if self.MIN < 99999999999:
            return self.MIN
        else:
            return -1

    def navigateAllPaths(self, index, sum, length):

        # DP check to see if a path of (index, sum) has already been initiated (no need to duplicate)
        if (index, sum) in self.DP_Set:
            return

        # Add to DP
        self.DP_Set.add((index, sum))

        # Check if the current length < self.MIN, GIVEN that all conditions and prereqs are satisfied
        if sum >= self.K and length < self.MIN:
            self.MIN = length

        # Base condition: Stop exploring paths once reached the last index element
        if index >= self.lenA:
            return

        # Navigate to other paths
        nextNum = self.A[index]
        # Nav to only next num
        if (index+1, nextNum) not in self.DP_Set:
            self.navigateAllPaths(index+1, nextNum, 1)

        # Nav to current sum + next num
        if (index+1, sum + nextNum) not in self.DP_Set:
            self.navigateAllPaths(index+1, sum + nextNum, length+1)
obj = Solution()
print obj.shortestSubarray(A = [2,-1,2,1,-2,3], K = 5)
# print obj.shortestSubarray(A = [1,2], K = 4)
# print obj.shortestSubarray(A = [1], K = 1)
