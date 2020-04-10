# ROYAL LEARNINGS :p
# Could do this using earlier memorization of matches (DP)
# Also did using KMP algorithm




# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

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
        return -1
class Solution(object):



    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == '':
            return 0


        return self.kmpController(haystack, needle)








    def multipleScoutsAlgo(self, haystack, needle):
        # A two dim array to store all this information
        starts = []
        currentPos = []

        # controller is equivalent to a scout who scouts for possible pointer candidates
        # criterion for thhe candidate: start the same as the needle's start
        for controller in range(len(haystack)):

            # if criteria met for the needle start, spawn a pointer which looks into this
            # Added optimiation: controller <= (len(haystack) - len(needle))
            #   This optim ensures that we are only adding new candidates till len(big)-len(small), as after that new candidates will not even make a diff as the string would be less than small / needle and hence not possible
            if controller <= (len(haystack) - len(needle)) and haystack[controller] == needle[0]:
                starts.append(controller)
                currentPos.append(0)

            # now, for all the scouted candidates (pointers), chheck their regular progress about their match to needle
            # if any of the candidate falters, remove them from the list
            # for i in range(len(starts)):
            i = 0
            while i < len(starts):
                if needle[currentPos[i]] == haystack[controller]:
                    currentPos[i] += 1
                    if currentPos[i] == len(needle):
                        return starts[i]
                else:
                    # optimize this to make it O(1)
                    starts.pop(i)
                    currentPos.pop(i)
                    i -= 1
                i += 1
        return -1

    def kmpCreatePrefixSuffixIndex(self, s):

        if len(s) == 1:
            return [0]

        outIndex = [0]*len(s)
        backwardPointer = 0
        forwardPointer = 1

        while forwardPointer < len(s):

            if s[forwardPointer] == s[backwardPointer]:
                outIndex[forwardPointer] = backwardPointer + 1
                backwardPointer += 1
                forwardPointer += 1
            else:
                if backwardPointer == 0:
                    forwardPointer += 1
                else:
                    backwardPointer = outIndex[backwardPointer-1]


        return outIndex

    def kmpController(self, s, pattern):

        patternIndex = self.kmpCreatePrefixSuffixIndex(pattern)

        sPointer = 0
        patternPointer = 0

        while (sPointer < len(s) and patternPointer < len(pattern)):

            if s[sPointer] == pattern[patternPointer]:
                sPointer += 1
                patternPointer += 1
                if patternPointer == len(pattern):
                    return sPointer - len(pattern)
            else:
                if patternPointer == 0:
                    sPointer += 1
                else:
                    patternPointer = patternIndex[patternPointer-1]
        return -1


obj = Solution()
print obj.strStr("aaaaaaaaaa", "aaaaaaaa")
print obj.strStr("abababc", "ababc")

# print obj.kmpCreatePrefixSuffixIndex("aabaabaaa")