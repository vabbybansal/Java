# Used two solns
# Main problems:
#   1) identifying the greedy soln
#   2) how to access the max and second max freq char again and again
#       1) using map, sorted lists
#       2) using dictionary heap which stores the char as key and freq as priority



# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].

class MaxHashHeap(object):

    # Invariant: Parent is always bigger than the children

    # Note: this is a special heap where the element is not the priority itself, but also another 'string/key' associated with that priority
    # The heapList stores the two in a tuple form of (priority, key)
    # All the manipulations in the heap are done via indices, so, the actual keys are hardly used
    # To access the keys in O(1), we store the key to index as a dictionary

    # List represented by a virtual heap. Elements are tuple (priority, elementKey)
    # heapList = []

    # Dictionary to store the indices of heap elements in the array
    # heapIndices = {}

    def __init__(self):
        self.heapList = list()
        self.heapIndices = {}

    def appendIntoHeap(self, tuplePriorityKey):
        # Append the new key at the end of the heap in the form of (priority, elementKey)
        self.heapList.append(tuplePriorityKey)
        # update the heapIndices dict with the index of the appended element
        self.heapIndices[tuplePriorityKey[1]] = len(self.heapList)-1

    def insertIntoHeap(self, tuplePriorityKey):

        # Insert at the end of the heap array
        self.appendIntoHeap(tuplePriorityKey)

        # Run maxHeapify on the last key
        self.maxHeapifyUp((len(self.heapList)-1))

    def hasParent(self, nodeIndex):
        if nodeIndex > 0:
            return True

    def getParentIndex(self, nodeIndex):
        return int((nodeIndex-1)/2)

    # Return the actual priority and not the tuple of priority, key
    def parentPriority(self, nodeIndex):
        return self.heapList[self.getParentIndex(nodeIndex)][0]

    def getLeftChildIndex(self, nodeIndex):
        return nodeIndex*2 + 1

    def getRightChildIndex(self, nodeIndex):
        return nodeIndex*2 + 2

    def hasLeftChild(self, nodeIndex):
        if self.getLeftChildIndex(nodeIndex) < len(self.heapList):
            return True

    def hasRightChild(self, nodeIndex):
        if self.getRightChildIndex(nodeIndex) < len(self.heapList):
            return True

    # Return the actual priority and not the tuple of priority, key
    def leftChildPriority(self, nodeIndex):
        return self.heapList[self.getLeftChildIndex(nodeIndex)][0]

    # Return the actual priority and not the tuple of priority, key
    def rightChildPriority(self, nodeIndex):
        return self.heapList[self.getRightChildIndex(nodeIndex)][0]

    # Correct the position of a single violation in the maxHeap by swapping parents and children
    def maxHeapifyUp(self, nodeIndex):

        # if parent is smaller than the child, swap them
        while(self.hasParent(nodeIndex)) and self.parentPriority(nodeIndex) < self.heapList[nodeIndex][0]:
            self.swap(self.getParentIndex(nodeIndex), nodeIndex)
            nodeIndex = self.getParentIndex(nodeIndex)

    # Correct the position of a single violation in the maxHeap by swapping parents and children
    def maxHeapifyDown(self, nodeIndex):

        # Check only if there is a child (left child first)
        while self.hasLeftChild(nodeIndex):
            biggerChildIndex = self.getLeftChildIndex(nodeIndex)

            # Check if we also have right child
            if self.hasRightChild(nodeIndex) and self.rightChildPriority(nodeIndex) > self.leftChildPriority(nodeIndex):
                biggerChildIndex = self.getRightChildIndex(nodeIndex)

            if self.heapList[nodeIndex][0] < self.heapList[biggerChildIndex][0]:
                self.swap(nodeIndex, biggerChildIndex)
                nodeIndex = biggerChildIndex
            else:
                return

    # Swap the parent and child nodes
    def swap(self, parentIndex, childIndex):

        tempVal = self.heapList[parentIndex]
        self.heapList[parentIndex] = self.heapList[childIndex]
        self.heapList[childIndex] = tempVal

        # once elements swapped, also update the indices in the heapIndices dictionary
        self.heapIndices[self.heapList[parentIndex][1]] = parentIndex
        self.heapIndices[self.heapList[childIndex][1]] = childIndex


    def popMax(self):

        if len(self.heapList) == 0:
            return None

        # If the max element has left child, start the process
        # Swap first element(max) with the last one, pop last, and run maxHeapify on the first element
        if self.hasLeftChild(0):
            self.swap(0, (len(self.heapList)-1))
            popped = self.heapList.pop()
            self.maxHeapifyDown(0)
        elif len(self.heapList) == 1:
            popped = self.heapList.pop()
            # Update the dictionary, remove the element from the map
        del self.heapIndices[popped[1]]

        return popped

    def changeVal(self, newValTuple):

        key = newValTuple[1]
        newPriority = newValTuple[0]
        currentIndex = self.heapIndices[key]
        currentPriority = self.heapList[currentIndex][0]

        # If the new node value is less than the current node value, then replace and do maxHeapfy downwards
        if newPriority < currentPriority:
            # since tuples are mutable, create a new tuple
            self.heapList[currentIndex] = (newPriority, key)
            # self.heapList[currentIndex][0] = newPriority

            # self.heapIndices[key] = # index still is the same
            self.maxHeapifyDown(currentIndex)
        # If the new node value is more than the current node value, then replace and do maxHeapfy upwards
        elif newPriority  > currentPriority:
            # self.heapList[currentIndex][0] = newPriority
            self.heapList[currentIndex] = (newPriority, key)
            self.maxHeapifyUp(currentIndex)
        else:
            return

    # def deleteIndex(self, nodeIndex):
    #
    #     # if it is the last element, simply pop
    #     if nodeIndex == len(self.heapList) - 1:
    #         popped = self.heapList.pop()
    #         del self.heapIndices[popped[1]]
    #         return
    #
    #     # The item at index to be removed has to be exchanged with last the last item and the last item can then be popped out
    #     # Why this works? If we remove the last item from a max/min heap, it still retains its max / min property
    #     # Also, we can handle one violation using maxHeapify methods
    #     # This is the same as exchanging the node with the last, popping out last element and running maxHeapify
    #
    #     # Remove last element
    #     lastElm = self.heapList.pop()
    #     self.heapIndices[lastElm[1]]
    #
    #     # Run changeVal
    #     self.changeVal(nodeIndex, lastElm)

    def deleteElm(self, key):

        currentIndex = self.heapIndices[key]

        # if it is the last element, simply pop
        if currentIndex == len(self.heapList) - 1:
            popped = self.heapList.pop()
            del self.heapIndices[key]
            return

        # The item at index to be removed has to be exchanged with last the last item and the last item can then be popped out
        # Why this works? If we remove the last item from a max/min heap, it still retains its max / min property
        # Also, we can handle one violation using maxHeapify methods
        # This is the same as exchanging the node with the last, popping out last element and running maxHeapify

        # Remove last element
        del self.heapIndices[key]

        # Change val at currentIndex to last elm and pop last element
        lastElmIndex = len(self.heapList) - 1
        lastElmKey = self.heapList[lastElmIndex][1]
        lastElmPriority = self.heapList[lastElmIndex][0]

        self.heapList.pop()
        # self.heapList[currentIndex][0] = lastElmPriority
        # since tuples are mutable, create a new tuple to reflect changes in a tuple
        self.heapList[currentIndex] = (self.heapList[currentIndex][0], lastElmKey)
        # self.heapList[currentIndex][1] = lastElmKey
        self.heapIndices[lastElmKey] = currentIndex

        # Run changeVal
        self.changeVal((lastElmPriority, lastElmKey))

class Solution(object):

    def setAdjust(self, poppedElm, freq, freqSetDict):

        if freq not in freqSetDict:
            freqSetDict[freq] = set()
        freqSetDict[freq].add(poppedElm)

    def handleSortedListIntrusion(self, pointer, sortedList, listMappedListOfKeys):

        # case 1: first element < second element (and maybe other elms later after 1st index)
        while (pointer+1) < len(sortedList) and sortedList[pointer] < sortedList[pointer + 1]:

            if sortedList[pointer] < sortedList[pointer+1]:
                tempNum = sortedList[pointer]
                tempMappedKey = listMappedListOfKeys[pointer]

                sortedList[pointer] = sortedList[pointer + 1]
                listMappedListOfKeys[pointer] = listMappedListOfKeys[pointer + 1]

                sortedList[pointer + 1] = tempNum
                listMappedListOfKeys[pointer + 1] = tempMappedKey
                pointer += 1

        # if last element is zero, remove it
        if sortedList[-1] == 0:
            sortedList.pop()
            listMappedListOfKeys.pop()

        # case 2: first element > second element => do nothing

        # case 3: first two elements same => do nothing



    def reorganizeString_01(self, S):
        """
        :type S: str
        :rtype: str
        """

        # init char freq dictionary
        charFreq = dict()
        # O(n)
        for char in S:
            if char not in charFreq:
                charFreq[char] = 0
            charFreq[char] += 1

        # init freq-Set Dict
        freqSetDict = dict()
        sortedFreqs = []
        sortedChars = []
        # O(alog(a))
        for key in charFreq:
            val = charFreq[key]
            if val not in freqSetDict:
                freqSetDict[val] = set()
            freqSetDict[val].add(key)

            # sortedFreqs.append(val)
            pointer = 0
            while pointer < len(sortedFreqs):
                if sortedFreqs[pointer] > val:
                    pointer += 1
                else:
                    break
            sortedFreqs.insert(pointer, val)
            sortedChars.insert(pointer, key)


        # start removal
        # O(n * a)
        strOut = ''
        lastChar = ''
        for i in range(len(S)):
            # if num of elements to be added is greater than 1 and only one element is left to bbe added, surely, we cannot have a string with non equal consecutive chars
            if len(S) - (i) > 1 and len(sortedFreqs) == 1:
                return ''

            topFreqChar = sortedChars[0]
            if lastChar != topFreqChar:
                strOut += topFreqChar
                lastChar = topFreqChar
                sortedFreqs[0] -= 1
                self.handleSortedListIntrusion(0, sortedFreqs, sortedChars)
            else:
                strOut += sortedChars[1]
                lastChar = sortedChars[1]
                sortedFreqs[1] -= 1
                self.handleSortedListIntrusion(1, sortedFreqs, sortedChars)

        # O(n) + O(a*log(a)) + O(n*a) = O(a*(n+log(a)))
        return strOut

    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        # init char freq dictionary
        charFreq = dict()
        # O(n)
        for char in S:
            if char not in charFreq:
                charFreq[char] = 0
            charFreq[char] += 1

        # Create a max hash table heap to store chars with their freq as their priorities
        maxHeap = MaxHashHeap()
        # O(a)
        for char in charFreq:
            maxHeap.insertIntoHeap((charFreq[char], char))


        outString = ''
        lastMaxChar = ''
        lastMaxPriority = 0

        # Pop max out of the heap consecutively for creating the string, thn update its freq
        # Note that, once we get out a, no need to immediately adding it to the heap, as we anyway want the next high freq char and not a, so next time simply pop the second highest and add a back and so on
        # O(n*log(a))
        for i in range(len(S)):

            currentMaxTuple = maxHeap.popMax()

            if currentMaxTuple == None and lastMaxPriority > 1:
                return ''

            currentMaxChar = currentMaxTuple[1]
            currentMaxPriority = currentMaxTuple[0]

            outString += currentMaxChar

            # add the last max char back to heap, if the count was more than 1
            if lastMaxPriority > 1:
                maxHeap.insertIntoHeap((lastMaxPriority-1, lastMaxChar))

            lastMaxChar = currentMaxChar
            lastMaxPriority = currentMaxPriority

        # O(n) + O(a) + O(n*log(a)) = O(n*log(a))

        return outString

obj = Solution()
print obj.reorganizeString("aaab")
print obj.reorganizeString("vvvlo")
print obj.reorganizeString("bfrbs")
print obj.reorganizeString("aaab")

