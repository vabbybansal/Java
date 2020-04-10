# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
# #
# # We may rotate the i-th domino, so that A[i] and B[i] swap values.
# #
# # Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
# #
# # If it cannot be done, return -1.



class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """


        aFlipUp = 0
        aFlipDown = 1
        bFlipUp = 1
        bFlipDown = 0

        a = A[0]
        b = B[0]
        aContinue = True
        bContinue = True

        for i in range(1, len(A)):

            # if a has been seen in all indices till now, then continue
            if aContinue:
                if A[i] == a or B[i] == a:
                    # Do something
                    if A[i] != a:
                        aFlipUp += 1
                    if B[i] != a:
                        aFlipDown += 1
                else:
                    aContinue = False

            # if a has been seen in all indices till now, then continue
            if bContinue:
                if A[i] == b or B[i] == b:
                    # Do something
                    if A[i] != b:
                        bFlipUp += 1
                    if B[i] != b:
                        bFlipDown += 1
                else:
                    bContinue = False

            if aContinue == False and bContinue == False:
                return -1

        outMinA = None
        outMinB = None
        if aContinue:
            outMinA = min(aFlipUp, len(A)-aFlipUp, aFlipDown, len(A)-aFlipDown)

        if bContinue:
            outMinB = min(bFlipUp, len(B)-bFlipUp, bFlipDown, len(B)-bFlipDown)

        if outMinA != None and outMinB != None:
            return min(outMinA, outMinB)
        elif outMinA is None:
            return outMinB
        else:
            return outMinA



obj = Solution()
# print obj.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2])
# print obj.minDominoRotations([2,2,2,3,3], [5,2,2,2,2])
print obj.minDominoRotations(
    [1,2,1,1,1,2,2,2],
    [2,1,2,2,2,2,2,2]
)