# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
#
# Note:
# The length of A and B will be between 1 and 10000.


# class Solution(object):
#
#     def createKMPSubStringArr(self, subString):
#
#         KMP_substring_arr = [0]*len(subString)
#
#         # if the length of thhe substring itself is 1 or lower, simply send the array of zeros
#         if len(subString) <= 1:
#             return KMP_substring_arr
#
#         forwardPointer = 1
#         backwardPointer = 0
#
#         while forwardPointer < len(subString):
#             # if the elements at the forward and backward pointerz are the same, then the KMP array element at forwardPointer = KMP array element at backwardPointer + 1
#             if subString[forwardPointer] == subString[backwardPointer]:
#                 KMP_substring_arr[forwardPointer] = backwardPointer + 1
#
#                 # increment forward and backward pointers
#                 forwardPointer += 1
#                 backwardPointer += 1
#
#             else:
#                 if backwardPointer == 0:
#                     forwardPointer += 1
#                 else:
#                     backwardPointer = KMP_substring_arr[backwardPointer-1]
#
#         return KMP_substring_arr
#
#
#
#     def repeatedStringMatch(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: int
#         """
#
#         # A - superString
#         # B - subString
#
#         self.KMPSubStringArr = self.createKMPSubStringArr(B)
#
#         aP = 0
#         bP = 0
#         repeats = 1
#         aOrig = A
#
#         while aP < len(A) and bP < len(B):
#
#             x = A[aP]
#             y = B[bP]
#
#             if A[aP] == B[bP]:
#                 aP += 1
#                 bP += 1
#                 if bP == len(B):
#                     return repeats
#             else:
#                 repeats = 1
#                 # A = aOrig
#                 if bP == 0:
#                     aP += 1
#                 else:
#                     bP = self.KMPSubStringArr[bP - 1]
#
#             if bP > 0 and aP == len(A):
#                 aP = 0
#                 repeats += 1
#
#
#         return -1

# class Solution(object):
#     def repeatedStringMatch(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: int
#         """
#
#         replicates = 1
#         aStart = 0
#         aP = 0
#         bP = 0
#         aLen = len(A)
#
#         while aStart < aLen and bP < len(B):
#
#             if A[aP] == B[bP]:
#                 aP += 1
#                 bP += 1
#
#                 if bP == len(B):
#                     return replicates
#                 if aP == len(A):
#                     aP = 0
#                     replicates += 1
#             else:
#                 aStart += 1
#                 replicates = 1
#                 bP = 0
#                 aP = aStart
#         return -1

class KMP(object):
    def createKMPSubStringArr(self, subString):

        KMP_substring_arr = [0]*len(subString)

        # if the length of thhe substring itself is 1 or lower, simply send the array of zeros
        if len(subString) <= 1:
            return KMP_substring_arr

        forwardPointer = 1
        backwardPointer = 0

        while forwardPointer < len(subString):
            # if the elements at the forward and backward pointerz are the same, then the KMP array element at forwardPointer = KMP array element at backwardPointer + 1
            if subString[forwardPointer] == subString[backwardPointer]:
                KMP_substring_arr[forwardPointer] = backwardPointer + 1

                # increment forward and backward pointers
                forwardPointer += 1
                backwardPointer += 1

            else:
                if backwardPointer == 0:
                    forwardPointer += 1
                else:
                    backwardPointer = KMP_substring_arr[backwardPointer-1]

        return KMP_substring_arr

    def doKMPSearch(self, superString, subString):

        superP = 0
        subP = 0
        kmpSubArray = self.createKMPSubStringArr(subString)

        while superP < len(superString) and subP < len(subString):

            if superString[superP] == subString[subP]:
                superP += 1
                subP += 1
                if subP == len(subString):
                    return superP - len(subString)
            else:
                if subP > 0:
                    subP = kmpSubArray[subP-1]
                else:
                    superP += 1




class Solution(object):

    def createKMPSubStringArr(self, subString):

            KMP_substring_arr = [0]*len(subString)

            # if the length of thhe substring itself is 1 or lower, simply send the array of zeros
            if len(subString) <= 1:
                return KMP_substring_arr

            forwardPointer = 1
            backwardPointer = 0

            while forwardPointer < len(subString):
                # if the elements at the forward and backward pointerz are the same, then the KMP array element at forwardPointer = KMP array element at backwardPointer + 1
                if subString[forwardPointer] == subString[backwardPointer]:
                    KMP_substring_arr[forwardPointer] = backwardPointer + 1

                    # increment forward and backward pointers
                    forwardPointer += 1
                    backwardPointer += 1

                else:
                    if backwardPointer == 0:
                        forwardPointer += 1
                    else:
                        backwardPointer = KMP_substring_arr[backwardPointer-1]

            return KMP_substring_arr

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        replicates = 1
        aStart = 0
        aP = 0
        bP = 0
        aLen = len(A)

        KMP_Array = self.createKMPSubStringArr(B)

        while aStart < aLen and bP < len(B):

            if A[aP] == B[bP]:
                aP += 1
                bP += 1

                if bP == len(B):
                    return replicates
                if aP == len(A):
                    aP = 0
                    replicates += 1
            else:
                if bP > 0:
                    delta = bP - KMP_Array[bP-1]
                    bP = KMP_Array[bP-1]
                    # replicates = 1
                    aStart = aStart + delta
                else:
                    aStart += 1
                    replicates = 1
                    bP = 0
                    aP = aStart
        return -1

# obj = Solution()
# print obj.repeatedStringMatch("abcd", "cdabcdab")
# print obj.repeatedStringMatch("abc", "cabcabca")
# print obj.repeatedStringMatch("aabaa", "aaab")
# "ababab"
# "ababac"
 # 001230

# print obj.strStr("aaaaaaaaaa", "aaaaaaaa")
# print obj.strStr("abababc", "ababc")

kmp = KMP()
print kmp.doKMPSearch("aaaaaaaaaa", "aaaaaaaa")
print kmp.doKMPSearch("abababc", "ababc")