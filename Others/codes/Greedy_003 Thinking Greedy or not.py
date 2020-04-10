# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.


# LEARNING
# THINKING ABOUT IT
# This seems the opposite of greedy algorithm. The input list of words is not told to have any structural tenets which could be utilized to create a greedy approach / heuristic. We might have to explore all paths possible, which should be completely opposite from Greedy
# update: maybe misread the problem, but the thought that greedy and exploring all paths are perpendicular to each other should be completely valid