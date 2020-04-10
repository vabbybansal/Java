# Learnings
# Nice use of 'interval window', not really a sliding window, but amazing interval window

# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
#
# Note:
#
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # pivots is the interval window
        pivots = [-99999999999]
        outs = [0]*len(S)

        for i in range(len(S)):
            char = S[i]
            if char == C:
                pivots.append(i)

        pivots.append(99999999999)

        # pointers on the pivots interval window
        lower = 0
        upper = 1

        for i in range(len(S)):
            outs[i] = min(i-pivots[lower], pivots[upper]-i)

            # check if the upper pointer overpasses the next char C position, then update
            if i >= pivots[upper]:
                lower+=1
                upper+=1

        return outs

obj = Solution()
print obj.shortestToChar(S = "loveleetcode", C = 'e')


