# DP
# HUGE LEARNING:
# I thought that we do not need memorization / DP because once we get a True (valid path to thhe end), we simply have to bubble up to the head and hence the memory of true for all the nodes in the pathh wont be used
# BUT, at least the memory of False paths can be used
# Once a true is found, no need to look, bbut in the meantime, we ll find many falses which will repeat, that is, here, a lot of 'locations' do not have any path and we are memorizing that to be used later


# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#s
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#
#         s_set = set()
#         word_set = set()
#         for char in s:
#             s_set.add(char)
#         for word in wordDict:
#             for char in word:
#                 word_set.add(char)
#         for char in s_set:
#             if char not in word_set:
#                 return False
#
#
#
#         len_string = len(s)
#         word_alpb_start_map = dict()
#
#         for word in wordDict:
#             if word[0] not in word_alpb_start_map:
#                 word_alpb_start_map[word[0]] = set()
#             word_alpb_start_map[word[0]].add(word)
#
#         # sort all word indices to have longer words first to further optimize the code
#         for word_start in word_alpb_start_map:
#             temp_set = word_alpb_start_map[word_start]
#             temp_list = list(temp_set)
#             temp_list.sort(reverse=True)
#             word_alpb_start_map[word_start] = temp_list
#         print word_alpb_start_map
#
#         def check_if_word_fits(location, word):
#             if s[location:location+len(word)] == word:
#                 return True
#             else:
#                 return False
#
#         def check_location(location):
#
#             # Base condition: is location the end of string
#             if location == len_string:
#                 return True
#
#             # Character allocation
#             char = s[location]
#
#             # if character in map, then propogate further after checking word validity
#             if char in word_alpb_start_map:
#                 # iterate all words
#                 for word in word_alpb_start_map[char]:
#                     # check if word fits correctly
#                     if check_if_word_fits(location, word):
#                         # if word fits, then simply recursively propogate to the next location
#                         verdict = check_location(location + len(word))
#
#                         # proactively probe if returns true. if it does, then it means the path is found
#                         # since we do not need to check all paths, skip by returning true
#                         # Note that in case we had to return all paths or total number of paths, we would have to explore all paths and would not skip, hence not return True at this point, rather explore all words + utilize DP as well
#                         if verdict == True:
#                             return True
#
#             # if code reaches to this point for any of the locations, then it means, there is no valid word, hence return False
#             return False
#
#         return check_location(0)


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        MEM = {}
        s_set = set()
        word_set = set()
        for char in s:
            s_set.add(char)
        for word in wordDict:
            for char in word:
                word_set.add(char)
        for char in s_set:
            if char not in word_set:
                return False



        len_string = len(s)
        word_alpb_start_map = dict()

        for word in wordDict:
            if word[0] not in word_alpb_start_map:
                word_alpb_start_map[word[0]] = set()
            word_alpb_start_map[word[0]].add(word)

        # sort all word indices to have longer words first to further optimize the code
        for word_start in word_alpb_start_map:
            temp_set = word_alpb_start_map[word_start]
            temp_list = list(temp_set)
            temp_list.sort(reverse=True)
            word_alpb_start_map[word_start] = temp_list
        print word_alpb_start_map

        def check_if_word_fits(location, word):
            if s[location:location+len(word)] == word:
                return True
            else:
                return False

        def check_location(location):

            if location in MEM:
                return MEM[location]

            # Base condition: is location the end of string
            if location == len_string:
                return True

            # Character allocation
            char = s[location]

            # if character in map, then propogate further after checking word validity
            if char in word_alpb_start_map:
                # iterate all words
                for word in word_alpb_start_map[char]:
                    # check if word fits correctly
                    if check_if_word_fits(location, word):
                        # if word fits, then simply recursively propogate to the next location
                        verdict = check_location(location + len(word))

                        # proactively probe if returns true. if it does, then it means the path is found
                        # since we do not need to check all paths, skip by returning true
                        # Note that in case we had to return all paths or total number of paths, we would have to explore all paths and would not skip, hence not return True at this point, rather explore all words + utilize DP as well
                        if verdict == True:
                            MEM[location] = True
                            return True

            # if code reaches to this point for any of the locations, then it means, there is no valid word, hence return False
            MEM[location] = False
            return False

        return check_location(0)


obj = Solution()
# print obj.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
print obj.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
# print obj.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])
