# DP
# MAJOR LEARNINGS:
#     - Think of the correct format of the recursive function, that is, should I add increment and then send or should I send and check increment in top of function
#     - In general, easier format = begining base case should which should check for validity instead of check for validity while calling the function recursively later on
#     - While calling the recursive function later in the code, simply go and call with increment, without checking at this point


# class Solution(object):
#     def numDecodings(self, s):
#
#         l = len(s)
#         map_alpha = {}
#         for i in range(26):
#             map_alpha[str(i+1)] = str(unichr(97+i))
#
#         outset = set()
#
#         def add(num, pos, code):
#
#             # Valid code
#             if pos == l:
#                 outset.add(code)
#                 return
#             if num == 2 and pos == l-1:
#                 return
#
#             if s[pos: pos+num] not in map_alpha:
#                 return
#
#
#             code += map_alpha[s[pos:pos+num]]
#
#             pos += num
#
#             add(1, pos, code)
#             add(2, pos, code)
#
#
#         add(1, 0, '')
#         add(2, 0, '')
#
#         return len(outset)

# class Solution(object):
#     def numDecodings(self, s):
#
#         l = len(s)
#         map_alpha = {}
#         for i in range(26):
#             map_alpha[str(i+1)] = str(unichr(97+i))
#
#         outset = set()
#
#         def add(increment, pos):
#
#             # Check the new state
#
#             # Base case of incorrect path [current position > l] [stop further propagation]
#             if pos > l:
#                 return 0
#
#             # Added alphabets should be valid code [a-z]
#             if s[pos-increment:pos] not in map_alpha:
#                 return 0
#
#             # Base Case of correct end of path [stoppage and return 1]
#             # end of string and the new alphabets are valid
#             if pos == l:
#                 return 1
#
#
#
#             left_paths = add(1, pos + 1)
#             right_paths = add(2, pos + 2)
#
#             # paths value at this point is the total path at this particular node
#             return left_paths + right_paths
#
#         one = add(1, 1)
#         two = add(2, 2)
#
#         return one + two

class Solution(object):
    def numDecodings(self, s):

        l = len(s)
        map_alpha = {}
        for i in range(26):
            map_alpha[str(i+1)] = str(unichr(97+i))
        MEM = {}

        outset = set()

        def add(increment, pos):



            # Check the new state

            # Base case of incorrect path [current position > l] [stop further propagation]
            if pos > l:
                return 0

            # Added alphabets should be valid code [a-z]
            if s[pos-increment:pos] not in map_alpha:
                return 0

            # Base Case of correct end of path [stoppage and return 1]
            # end of string and the new alphabets are valid
            if pos == l:
                return 1

            # Check for memory
            if pos in MEM:
                return MEM[pos]

            left_paths = add(1, pos + 1)
            right_paths = add(2, pos + 2)

            # paths value at this point is the total path at this particular node
            MEM[pos] = left_paths + right_paths
            return left_paths + right_paths

        one = add(1, 1)
        two = add(2, 2)

        return one + two

obj = Solution()
print obj.numDecodings("611")