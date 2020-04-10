class TrieNode(object):
    def __init__(self):
        self.charDict = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        pointer = self.root

        for char in word:
            if char not in pointer.charDict:
                pointer.charDict[char] = TrieNode()
            pointer = pointer.charDict[char]
        pointer.endOfWord = True

    def navigate(self, word):
        pointer = self.root

        for char in word:
            if char in pointer.charDict:
                pointer = pointer.charDict[char]
            else:
                return False
        return pointer

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        navigateResult = self.navigate(word)
        if navigateResult != False:
            return navigateResult.endOfWord
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        navigateResult = self.navigate(prefix)
        if navigateResult != False:
            return True
        else:
            return False



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
obj.insert("abcd")
obj.insert("abcde")
obj.insert("bbcd")
print obj.search("ancd")
print obj.search("abcd")
print obj.startsWith("a")
print obj.startsWith("b")
print obj.startsWith("c")
print obj.startsWith("bbc")