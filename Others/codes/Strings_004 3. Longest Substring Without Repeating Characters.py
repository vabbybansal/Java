# Strings using a sliding window logic
# Sets can be used to check if an element already exists in a string or not

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        startPointer = 0
        endPointer = 0

        # DICT DOESN't WORK SINCE WE WILL HAVE TO UPDATE DICT AND REMOVE chars till the startpoint stops duplication which is again O(n), then manual traversal works the same way
        # Stores the index of all characters in the current subsequence
        # currentCharsHashTable = {}

        currentSet = set()

        # Stores the current max len
        currentMax = 0

        while startPointer < len(s) and endPointer < len(s):

            currentChar = s[endPointer]

            # if current char is not already in the current set, it means, the bigger string is still valid
            if currentChar not in currentSet:

                # Add to the visited set
                currentSet.add(currentChar)

                # update max
                newLen = endPointer - startPointer + 1
                if currentMax < newLen:
                    currentMax = newLen


            # If current char already in the set, increment startPointer to the place where thhe earlier duplicate of current character exists + 1 [no need to update max len, as the new length is effectively less than equal to the current len]
            else:
                while s[startPointer] != currentChar:
                    # remove the 'removed' visited chars from visited set
                    currentSet.remove(s[startPointer])
                    startPointer += 1
                # One more increment to the startPointer to go over the actual duplicated character
                # Also, no need to do an additional currentSet.remove since the currentChar is anyway in the string as of now, so works fine this way
                startPointer += 1


            # Update endpointer to go to the next character
            endPointer += 1

        return currentMax

obj = Solution()
print obj.lengthOfLongestSubstring("bbbbb")

