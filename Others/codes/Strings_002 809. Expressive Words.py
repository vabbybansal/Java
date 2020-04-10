# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
#
# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.
#
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
#
# Given a list of query words, return the number of words that are stretchy.


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        out = 0
        for word in words:

            sPointer = 0
            wPointer = 0
            while sPointer < len(S) and wPointer < len(word):
                currentSChar = S[sPointer]
                currentWChar = word[wPointer]
                sPointerInitial = sPointer
                wPointerInitial = wPointer

                # Check if next possible and if char is same
                while sPointer+1 < len(S) and S[sPointer+1] == currentSChar:
                    sPointer += 1
                if word[wPointer] != S[sPointer]:
                    break
                # Check if next possible and if char is same
                while wPointer+1 < len(word) and word[wPointer+1] == currentWChar:
                    wPointer += 1

                lenSPointer = sPointer - sPointerInitial + 1
                lenWPointer = wPointer - wPointerInitial + 1
                if lenWPointer > lenSPointer or (lenSPointer != lenWPointer and lenSPointer<3):
                    break

                sPointer += 1
                wPointer += 1

            if sPointer == len(S) and wPointer == len(word):
                out += 1

        return out

obj = Solution()
# print obj.expressiveWords("heeellooo", ["hello", "hi", "helo"])
print obj.expressiveWords("heeellooo", ["hll"])
