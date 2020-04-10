# Stacks
# 2[b4[F]c] should mean that each of b, FFFF, c should be at the same level. How to ensure?
# put each calculate popped item in stack itself (that is, put FFFF back on the stack, so elms would be [b][FFFF][c]
# Otherwise, starting intuition could be that I ll remove popped stuff (FFFF) out and append to some global string, but then, it gets detached from it siblings b and c
# so, in stacks, to keep the siblings together, place them in subsequent elements



# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

# class Solution(object):
#
#     def genStringMultiple(self, s, multiple):
#
#         return s*multiple
#
#
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#
#         stack = []
#         popFlag = False
#         i = 0
#         decodedString = ''
#         STACK_CLEAR = 1
#
#         while s[i].isdigit() == False:
#             decodedString += s[i]
#             i += 1
#
#         while i < len(s):
#
#             char = s[i]
#
#             if char != ']':
#                 if char.isdigit():
#                     currentNumStr = char
#                     while s[i+1].isdigit():
#                         currentNumStr += s[i+1]
#                         i += 1
#                     # we have the number at this point
#                     num = int(currentNumStr)
#                     stack.append(num)
#                     i += 1
#
#                     continue
#
#                 # if the char is not ] or numeral, append the char in the stack
#                 stack.append(char)
#                 i += 1
#
#             else:
#                 # char == ]
#                 # Start popping till we get a [ and then multiply the string and store
#                 popped = stack.pop()
#                 if STACK_CLEAR == 1:
#                     currentStr = ''
#                 while popped != '[':
#                     currentStr = popped + currentStr
#                     popped = stack.pop()
#                 popNumeral = stack.pop()
#                 multipliedString = self.genStringMultiple(currentStr, popNumeral)
#
#                 # if the stack is clear then simply append this string to final decodedString
#                 if len(stack) == 0:
#                     decodedString += multipliedString
#                     STACK_CLEAR = 1
#                 # else, keep going with the currentStr
#                 else:
#                     STACK_CLEAR = 0
#                 i += 1
#
#         # if len(stack) != 0:
#
#
#         return decodedString

class Solution(object):

    def popCoded(self, currentStr, stack):

        popped = ''
        while popped != '[':
            currentStr = popped + currentStr
            popped = stack.pop()
        popNumeral = int(stack.pop())
        currentStr = self.genStringMultiple(currentStr, popNumeral)

        return currentStr

    def genStringMultiple(self, s, multiple):

        return s*multiple


    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        decodedString = ''
        currentStr = ''

        for char in s:

            if char != ']':

                # if the new element is a digit, and the last one was also a digit, append this one to the last one
                if char.isdigit():
                    # if the last element was also a digit, simply append this digit to the last one
                    if len(stack) > 0 and stack[-1].isdigit():
                        stack[-1] += char
                        continue
                stack.append(char)

            else:
                # the element is ']', so do a pop routine
                stack.append(self.popCoded(currentStr, stack))

        return ''.join(stack)


obj = Solution()
# print obj.decodeString("3[a]2[bc]")
# print obj.decodeString("3[a]2[bc]")
# print obj.decodeString("3[a]bb3[a]")
# print obj.decodeString("2[abc]3[cd]ef")
print obj.decodeString("3[a]2[b4[F]c]")
print obj.decodeString("leetcode")