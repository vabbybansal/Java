# Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.
#
# In C++, there are two types of comments, line comments, and block comments.
#
# The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.
#
# The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.
#
# The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.
#
# If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
#
# There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)
#
# It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.
#
# Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.
#
# After removing the comments from the source code, return the source code in the same format.
#
# Example 1:
# Input:
# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
#
# The line by line code is visualized as below:
# /*Test program */
# int main()
# {
# // variable declaration
# int a, b, c;
# /* This is a test
# multiline
# comment for
# testing */
# a = b + c;
# }
#
# Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
#
# The line by line code is visualized as below:
# int main()
# {
#
#     int a, b, c;
# a = b + c;
# }
#
# Explanation:
# The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
# Example 2:
# Input:
# source = ["a/*comment", "line", "more_comment*/b"]
# Output: ["ab"]
# Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].



class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        line = 0
        char = 0
        STAR_FLAG = False
        outFormatted = []
        blockCommentLineAffected = False
        blockCommentLineStart = None
        blockCommentLineEnd = None
        while line < len(source):

            char = 0
            lineFormatted = ''
            while char < len(source[line]):

                # if star_flag is True [currently in block comment] andnext char is not *, simply ignore
                if STAR_FLAG:
                    if source[line][char] != '*':
                        char += 1
                        continue
                    else:
                        # * is the last char then ignore
                        if char+1 < len(source[line]) and source[line][char+1] == '/':
                            blockCommentLineEnd = line
                            char += 2
                            STAR_FLAG = False
                        else:
                            char += 1
                            continue
                elif source[line][char] != '/':
                    lineFormatted += source[line][char]
                    char += 1
                    continue
                else:

                    # '/' is the last char
                    if char+1 >= len(source[line]):
                        lineFormatted += source[line][char]
                        char += 1
                    else:
                        # if the next character does not start the comment, simply continue
                        if source[line][char+1] != '/' and source[line][char+1] != '*':
                            lineFormatted += source[line][char]
                            char += 1
                        # if next character is '/' then its a line comment and ignore the rest of the line
                        elif source[line][char+1] == '/':
                            # break the loop and go to next line
                            # line += 1
                            break
                        # if the next char is *, we start the block comment
                        # elif source[line][char+1] == '*' and char+2 < len(source[line]) and source[line][char+2] == '/':
                        #     lineFormatted += '/*/'
                        #     char += 3
                        elif source[line][char+1] == '*':
                            blockCommentLineStart = line
                            STAR_FLAG = True
                            char += 2

            if len(lineFormatted) > 0:

                if blockCommentLineEnd != line:
                    outFormatted.append(lineFormatted)
                elif blockCommentLineStart == blockCommentLineEnd == line:
                    outFormatted.append(lineFormatted)
                elif blockCommentLineStart < blockCommentLineEnd and blockCommentLineEnd == line:
                    outFormatted[len(outFormatted)-1] += lineFormatted

            line += 1
            # blockCommentLineAffected = False
        return outFormatted

obj = Solution()
# print obj.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
# print obj.removeComments(["a/*comment", "line", "more_comment*/b"])
# print obj.removeComments(["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"])
print obj.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"])
# "class test{"
# "public: "
# "   int x = 1;"
# "   /*double y = 1;*/"
# "   char c;"
# "};"
[
    "struct Node{",
    "    /*/ declare members;/**/",
    "    int size;",
    "    /**/int val;",
    "};"
]