# We have two integer sequences A and B of the same non-zero length.
#
# We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.
#
# At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)
#
# Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.
#
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation:
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.

class Solution(object):

    MEM = set()

    def swapNumbers(self, A, B, i):
        temp = A[i]
        A[i] = B[i]
        B[i] = temp
        return A[i], B[i]

    def runAlgo(self, A, B, i, interchangePrvStates, swaps):

        a_past = A[i-1]
        b_past = B[i-1]

        for i in range(i, len(A)):
            a_current = A[i]
            b_current = B[i]

            # Problem with the current configuration
            if a_current <= a_past or b_current <= b_past:



                t = i
                while t >= 0:
                    t -= 1
                    if interchangePrvStates[t] == 1:
                        A_copy = A.copy()
                        B_copy = B.copy()
                        interchangePrvStates_copy = interchangePrvStates.copy()
                        self.swapNumbers(A_copy, B_copy, t)
                        interchangePrvStates_copy[t] = 0

                        self.runAlgo(self, A.copy(), B.copy(), t, interchangePrvStates_copy, swaps + 1)
                        # swaps += 1
                        break


                if b_current > a_past and a_current > b_past:
                    a_current, b_current = self.swapNumbers(A, B, i)
                    swaps += 1
                    # self.runAlgo(self, A.copy(), B.copy(), i, interchangePrvStates.copy(), swaps)



                #     # go back
                #     while i >= 0:
                #         i -= 1
                #         if interchangePrvStates[i] == 1:
                #             a_current, b_current = self.swapNumbers(A, B, i)
                #             swaps += 1
                #             break
                # else:
                #     a_current, b_current = self.swapNumbers(A, B, i)
                #     swaps += 1

            # Fine with the current configuration, then check if the swapped version is also fine and store the value
            else:
                if a_current <= b_past or b_current <= a_past:
                    interchangePrvStates[i] = 0
                else:
                    interchangePrvStates[i] = 1

            a_past = a_current
            b_past = b_current

        self.MEM.add(swaps)

        return swaps

    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        swaps = 0

        interchangePrvStates = [0]*len(A)
        interchangePrvStates[0] = 1
        i = 1

        self.runAlgo(A, B, i, interchangePrvStates, swaps)

        return min(self.MEM)



obj = Solution()
# print obj.minSwap([1,3,5,4], [1,2,3,7])
# print obj.minSwap(
#     [0,3,5,8,9],
#     [2,1,4,6,9]
# )

# print obj.minSwap(
#     [3,3,8,9,10],
#     [1,7,4,6,8]
# )
#
print obj.minSwap(
    [0,4,4,5,9],
    [0,1,6,8,10]
)

