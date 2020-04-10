# Learning
# I was able to find the solution using all paths at the very start. However, too adamant to use stacks to validate the parenthesis, which created unnecessary complexity. We can simply use strings
# PARENTHESIS LOGIC CAN BE DONE USING SIMPle COUNTS IN ADDITION TO STACKS
#   num_left_brackets >= num_right_brackets
#   num_left_brackets <= n and num_right_brackets <= n
#   validity: num_left_brackets == num_right_brackets
# I was trying to keep the paren sequence in a stack, but during addition of right bracket, I need to remove () from stack, bbut then how do we keep track of elements while recurison and backtracking, that is if I remove the elements at this stage, and come back to this stag elater using backtracking, my list / stack will not have the deleted elements, so I lost state / backtracking state?
# hence, never use stacks in recursion if you intend to remove stuff during recursion, coz backtracking wont have the correct state then

# ALSO, THINK ABOUT WHAT DATA STRUCTURE IS REQUIRED WHILE NAVIGATING AND BACKTRACKING. IF POSSIBLE, A CONSTANT INTEGER / STRING IS THE BEST. USE LIST / STACK ETC ONLY OF NEEDED
# ALSO THINK ABOUT CAN A DUPLICATE NODE BE GENERATED? HERE ALL PATHS LEAD TO DIFFERENT SEQUENCE HENCE CANT DO MEMOIZATION


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#     "((()))",
#     "(()())",
#     "(())()",
#     "()(())",
#     "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.n = n
        self.outList = []

        self.addParen('', 1, 0, 0)

        return self.outList


    def addParen(self, queueStr, iteration, numL, numR):

        # Base Case
        if iteration == 2*self.n + 1:
            if numL == numR:
                self.outList.append(queueStr)
            return

        # Validity
        if numR > numL:
            return
        if numL > self.n or numR > self.n:
            return

        # Navigation
        queueStr += '('
        self.addParen(queueStr, iteration+1, numL+1, numR)
        queueStr = queueStr[0:-1]

        queueStr += ')'
        self.addParen(queueStr, iteration+1, numL, numR+1)
        queueStr = queueStr[0:-1]


print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
print Solution().generateParenthesis(1)
print Solution().generateParenthesis(0)