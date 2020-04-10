# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
#
# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.


class Solution(object):

    mapF = {}
    mapQueries = {}

    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        outList = [0]*len(queries)

        for i in range(len(queries)):

            s = queries[i]
            wordCountMatch = 0
            if self.f(s) in self.mapQueries:
                outList[i] = self.mapQueries[self.f(s)]
                continue
            for w in words:
                if self.f(s) < self.f(w):
                    wordCountMatch += 1
            outList[i] = wordCountMatch
            self.mapQueries[self.f(s)] = wordCountMatch
        return outList

    def f(self, s):

        # Use if already calculated
        if s in self.mapF:
            return self.mapF[s]

        charMap = {}
        minChar = 'z'
        for char in s:
            if char not in charMap:
                if char < minChar:
                    minChar = char
                charMap[char] = 0
            charMap[char] += 1

        # Memorize
        self.mapF[s] = charMap[minChar]
        return charMap[minChar]


obj = Solution()
# print obj.numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"])
print obj.numSmallerByFrequency(
    ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"],
    ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
)