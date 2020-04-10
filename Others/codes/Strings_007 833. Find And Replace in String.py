# Learnings:
# 1) How to run a pointer in a list from start to various intervals to end: 0 - [2, 5, 10, 40] - 100
# 2) I am making changes to a string by replacing some index1-index2 to some other string with possibily different length.
# How to do this in O(n) by memorizing the deltas at each change using a hash map

# To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).
#
# Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.
#
# For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".
#
# Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.
#
# All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
#
# Example 1:
#
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".
# Example 2:
#
# Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
# "ec" doesn't starts at index 2 in the original S, so we do nothing.
# Notes:
#
# 0 <= indexes.length = sources.length = targets.length <= 100
# 0 < indexes[i] < S.length <= 1000
# All characters in given inputs are lowercase letters.

class Solution(object):
    def findReplaceStringOld(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """


        targets

        bools = [True]*len(indexes)
        outs = ['']*len(indexes)

        indeInitial = list(indexes)
        sourcesInitial = list(sources)
        targetsInitial = list(targets)
        indexes.sort()

        for i in range(len(indexes)):
            newInd = indexes[i]
            for j in range(len(indexes)):
                if indeInitial[j] == newInd:
                    sources[i] = sourcesInitial[j]
                    targets[i] = targetsInitial[j]
                    break




        for i in range(len(indexes)):

            pointerStart = indexes[i]
            source = sources[i]
            lenSource = len(source)

            for sourceIndex in range(lenSource):
                if S[pointerStart + sourceIndex] != source[sourceIndex]:
                    bools[i] = False
                    break

        stitchPointer = 0
        stitchedString = ''
        indexPointer = 0
        while stitchPointer < len(S):
            if indexPointer >= len(indexes):
                stitchedString += S[stitchPointer:]
                break
            if stitchPointer < indexes[indexPointer]:
                stitchedString += S[stitchPointer:indexes[indexPointer]]
                stitchPointer = indexes[indexPointer]
            elif stitchPointer == indexes[indexPointer]:
                if bools[indexPointer]:
                    stitchedString += targets[indexPointer]
                    stitchPointer += len(sources[indexPointer])
                    indexPointer += 1
                else:
                    stitchedString += S[stitchPointer]
                    stitchPointer += 1
                    indexPointer += 1

        return stitchedString

    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """




        bools = [True]*len(indexes)
        outs = ['']*len(indexes)

        for i in range(len(indexes)):

            pointerStart = indexes[i]
            source = sources[i]
            lenSource = len(source)

            for sourceIndex in range(lenSource):
                if S[pointerStart + sourceIndex] != source[sourceIndex]:
                    bools[i] = False
                    break

        outString = S
        done = {}
        for i in range(len(indexes)):

            if bools[i]:
                elm = indexes[i]
                for elmDone in done:
                    if elmDone < indexes[i]:
                        elm += done[elmDone]
                toBeReplacedString = sources[i]
                # print outString[elm:elm+len(toBeReplacedString)] == sources[i]

                replaceString = targets[i]
                lenReplaced = len(toBeReplacedString)
                lenReplacement = len(replaceString)
                deltaChanges = lenReplacement - lenReplaced

                done[indexes[i]] = deltaChanges
                outString = outString[0:elm] + replaceString + outString[elm+lenReplaced:]

        return outString

obj = Solution()
# print obj.findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"])
# print obj.findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"])
# print obj.findReplaceString("vmokgggqzp"
#                             ,[3,5,1]
#                             ,["kg","ggq","mo"]
#                             ,["s","so","bfr"])
# print obj.findReplaceString(
#     "emgzpmdoogscklvhtgmethuiscljkdoqewgvbulemuxgtrkgxy",
#     [33,42,9,16,40,2,5,22,0,37,29,11,18,7,47,44],
#     ["wg","xg","gs","tg","mu","gzp","md","uisc","em","ule","doqe","cklvh","meth","oo","gxy","tr"],
#     ["v","g","vh","b","o","anjn","npm","fro","vqu","nuv","qam","kdfldd","ilak","wy","pn","kl"]
# )

# print obj.findReplaceString(
#     "emgzpmdoogscklvhtgmethuiscljkdoqewgvbulemuxgtrkgxy",
#     [9,16,40,2,5,0,37],
#     ["gs","tg","mu","gzp","md","em","ule"],
#     ["vh","b","o","anjn","npm","vqu","nuv"]
# )

print obj.findReplaceString(
    "ejvzndtzncrelhedwlwiqgdbdgctgubzczgtovufncicjlwsmfdcrqeaghuevyexqdhffikvecuazrelofjmyjjznnjdkimbklrh",
    [69,79,15,19,58,92,27,64,4,72],
    ["ikv","lo","dw","iqgdbd","ue","kimbk","tgu","qd","ndt","ec"],
    ["tira","rko","oob","mlitiwj","zrj","onpp","ot","c","lm","qi"]
)

print obj.findReplaceString(
    "ejvzndtzncrelhedwlwiqgdbdgctgubzczgtovufncicjlwsmfdcrqeaghuevyexqdhffikvecuazrelofjmyjjznnjdkimbklrh",
    [69,79,15,19,58,92,27,64,72],
    ["ikv","lo","dw","iqgdbd","ue","kimbk","tgu","qd","ec"],
    ["tira","rko","oob","mlitiwj","zrj","onpp","ot","c","qi"]
)