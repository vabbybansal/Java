# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# class Stack(list):
#     def stackPush(self, elm):
#         self.append(elm)
#     def stackPop(self):
#         self.pop(-1)
#
# class Solution(object):
#     def backspaceCompare(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: bool
#         """
#
#         # Stack Way
#         # stackS = self.stackProcess(S)
#         # stackT = self.stackProcess(T)
#         #
#         # if len(stackS) != len(stackT):
#         #     return False
#         # else:
#         #     for i in range(len(stackS)):
#         #         if stackS[i] != stackT[i]:
#         #             return False
#
#         # Non Stack Way
#
#         return self.checkStringReverse(S, T)
#
#     def stackProcess(self, string):
#
#         stack = Stack()
#
#         for char in string:
#             if char == '#':
#                 if len(stack) > 0:
#                     stack.stackPop()
#             else:
#                 stack.stackPush(char)
#
#         return stack
#
#     def checkStringReverse(self, S, T):
#
#         lenIterate = max(len(S), len(T))
#
#         sPointer = len(S) - 1
#         tPointer = len(T) - 1
#         delsS = 0
#         delsT = 0
#
#         while sPointer >= 0 or tPointer >= 0:
#
#             s1 = S[sPointer]
#             t1 = T[tPointer]
#
#             if S[sPointer] != '#' and T[tPointer] != '#':
#                 if S[sPointer] != T[tPointer]:
#                     return False
#             else:
#                 while (sPointer >= 0 and S[sPointer] == '#') or delsS >0:
#                     if S[sPointer] == '#':
#                         delsS += 1
#                         sPointer -= 1
#                     else:
#                         sPointer -= 1
#                         delsS -= 1
#
#                 while (tPointer >= 0 and T[tPointer] == '#') or delsT >0:
#                     if T[tPointer] == '#':
#                         delsT += 1
#                         tPointer -= 1
#                     else:
#                         tPointer -= 1
#                         delsT -= 1
#
#                 if sPointer >= 0 and tPointer >= 0:
#                     if S[sPointer] != T[tPointer]:
#                         return False
#                 else:
#                     if sPointer >= 0 or tPointer >= 0:
#                         return False
#
#             sPointer -= 1
#             tPointer -= 1
#
#         if sPointer < 0 and tPointer < 0:
#             return True
#         else:
#             return False




obj = Solution()
# print obj.backspaceCompare("a##c", "#a#c")
# print obj.backspaceCompare(
#     "y#fo##f",
#     "y#f#o##f"
# )

# print obj.backspaceCompare("bxj###tw", "bxj##tw")
print obj.backspaceCompare("bbb#extm", "bbbextm")