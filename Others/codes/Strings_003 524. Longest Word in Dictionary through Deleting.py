# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

# DP
# class Solution(object):
#
#     def stringContains(self, super, sub):
#
#         lenSup = len(super)
#         lenSub = len(sub)
#
#         if lenSup < lenSub:
#             return False
#
#         if lenSub == 0:
#             return True
#
#         superP = 0
#         subP = 0
#
#         while superP < lenSup and subP < lenSub:
#             if sub[subP] not in self.superSet:
#                 return False
#             if sub[subP] == super[superP]:
#                 subP += 1
#                 if subP == lenSub:
#                     return True
#
#             superP += 1
#
#         return False
#
#     def stringContainsRecursionDriver(self, super, sub):
#
#         return self.stringContainsRecursion(super, sub, 0, 0)
#
#     # def memorize(self, super, superP, sub, subP, myReturn):
#         # Store the partial strings result
#         # self.MEM[super[superP:]+'__'+sub[subP:]] = True
#
#     def stringContainsRecursion(self, super, sub, superP, subP):
#
#         # superLeft = super[superP:]
#         # subLeft = sub[subP:]
#         if (super[superP:]+'__'+sub[subP:]) in self.MEM:
#             return self.MEM[super[superP:]+'__'+sub[subP:]]
#
#         if subP == len(sub):
#             return True
#
#         if len(super) - superP > 0 and len(sub) - subP > 0:
#
#             if sub[subP] == super[superP]:
#                 myReturn = self.stringContainsRecursion(super, sub, superP+1, subP+1)
#                 # Store the partial strings result
#                 self.MEM[super[superP:]+'__'+sub[subP:]] = myReturn
#                 return myReturn
#             else:
#                 myReturn = self.stringContainsRecursion(super, sub, superP+1, subP)
#                 # Store the partial strings result
#                 self.MEM[super[superP:]+'__'+sub[subP:]] = myReturn
#                 return myReturn
#         else:
#             return False
#
#
#     def findLongestWord(self, s, d):
#         """
#         :type s: str
#         :type d: List[str]
#         :rtype: str
#         """
#
#         self.superSet = set()
#         out = ""
#         lenSup = len(s)
#
#         self.MEM = {}
#
#         for char in s:
#             self.superSet.add(char)
#
#         for sub in d:
#             # contain = self.stringContains(s, sub)
#             contain = self.stringContainsRecursionDriver(s, sub)
#
#             if contain:
#                 lenSub = len(sub)
#                 lenOut = len(out)
#                 if lenSub > lenOut:
#                     out = sub
#                 elif lenSub == lenOut:
#                     out = min(sub, out)
#
#         return out


class Solution(object):

    def stringContains(self, super, sub):

        lenSup = len(super)
        lenSub = len(sub)

        if lenSup < lenSub:
            return False

        if lenSub == 0:
            return True

        superP = 0
        subP = 0

        while superP < lenSup and subP < lenSub:
            if sub[subP] not in self.superSet:
                return False
            if sub[subP] == super[superP]:
                subP += 1
                if subP == lenSub:
                    return True

            superP += 1

        return False


    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        self.superSet = set()
        out = ""
        lenSup = len(s)


        for char in s:
            self.superSet.add(char)

        for sub in d:
            if len(sub) < len(out):
                continue
            contain = self.stringContains(s, sub)

            if contain:
                lenSub = len(sub)
                lenOut = len(out)
                if lenSub > lenOut:
                    out = sub
                elif lenSub == lenOut:
                    out = min(sub, out)

        return out

obj = Solution()
print obj.findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
print obj.findLongestWord("abpcplea", ["a","b","c"])
print obj.findLongestWord("", ["b","a"])