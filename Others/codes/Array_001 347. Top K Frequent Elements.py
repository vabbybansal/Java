# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#

# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
class MinHeap(object):

    # Invariant: Parent is always bigger than the children
    heapList = []

    def __init__(self):
        self.heapList = list()

    def insertIntoHeap(self, key):

        # Insert at the end of the heap array
        self.heapList.append(key)

        # Run maxHeapify on the last key
        self.minHeapifyUp((len(self.heapList)-1))

    def hasParent(self, nodeIndex):
        if nodeIndex > 0:
            return True

    def getParentIndex(self, nodeIndex):
        return int((nodeIndex-1)/2)

    def parent(self, nodeIndex):
        return self.heapList[self.getParentIndex(nodeIndex)]

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

    def leftChild(self, nodeIndex):
        return self.heapList[self.getLeftChildIndex(nodeIndex)]

    def rightChild(self, nodeIndex):
        return self.heapList[self.getRightChildIndex(nodeIndex)]

    # Correct the position of a single violation in the maxHeap by swapping parents and children
    def minHeapifyUp(self, nodeIndex):

        # if parent is smaller than the child, swap them
        while(self.hasParent(nodeIndex)) and self.parent(nodeIndex) > self.heapList[nodeIndex]:
            self.swap(self.getParentIndex(nodeIndex), nodeIndex)
            nodeIndex = self.getParentIndex(nodeIndex)

    # Correct the position of a single violation in the maxHeap by swapping parents and children
    def minHeapifyDown(self, nodeIndex):

        # Check only if there is a child (left child first)
        while self.hasLeftChild(nodeIndex):
            smallerChildIndex = self.getLeftChildIndex(nodeIndex)

            # Check if we also have right child
            if self.hasRightChild(nodeIndex) and self.rightChild(nodeIndex) < self.leftChild(nodeIndex):
                smallerChildIndex = self.getRightChildIndex(nodeIndex)

            if self.heapList[nodeIndex] > self.heapList[smallerChildIndex]:
                self.swap(nodeIndex, smallerChildIndex)
                nodeIndex = smallerChildIndex
            else:
                return

    # Swap the parent and child nodes
    def swap(self, parentIndex, childIndex):

        tempVal = self.heapList[parentIndex]
        self.heapList[parentIndex] = self.heapList[childIndex]
        self.heapList[childIndex] = tempVal

    def popMin(self):

        if len(self.heapList) == 0:
            return False

        # If the max element has left child, start the process
        # Swap first element(max) with the last one, pop last, and run maxHeapify on the first element
        if self.hasLeftChild(0):
            self.swap(0, (len(self.heapList)-1))
            popped = self.heapList.pop()
            self.minHeapifyDown(0)
        elif len(self.heapList) == 1:
            popped = self.heapList.pop()

        return popped

    def changeVal(self, nodeIndex, newVal):

        # If the new node value is less than the current node value, then replace and do minHeapfy downwards
        if newVal > self.heapList[nodeIndex]:
            self.heapList[nodeIndex] = newVal
            self.minHeapifyDown(nodeIndex)
        # If the new node value is more than the current node value, then replace and do minHeapfy upwards
        elif newVal < self.heapList[nodeIndex]:
            self.heapList[nodeIndex] = newVal
            self.minHeapifyUp(nodeIndex)
        else:
            return

    def deleteIndex(self, nodeIndex):

        # The item at index to be removed has to be exchanged with last the last item and the last item can then be popped out
        # Why this works? If we remove the last item from a max/min heap, it still retains its max / min property
        # Also, we can handle one violation using maxHeapify methods
        # This is the same as exchanging the node with the last, popping out last element and running maxHeapify

        # Remove last element
        lastElm = self.heapList.pop()

        # Run changeVal
        self.changeVal(nodeIndex, lastElm)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freqMap = {}
        for elm in nums:
            if elm not in freqMap:
                freqMap[elm] = 1
            else:
                freqMap[elm] += 1

        freqVals = freqMap.values()

        myMinHeap = MinHeap()

        for elm in freqVals:

            if len(myMinHeap.heapList) == k and elm < myMinHeap.heapList[0]:
                continue

            myMinHeap.insertIntoHeap(elm)
            if len(myMinHeap.heapList) > k:
                myMinHeap.popMin()

        cutoffFreq = myMinHeap.popMin()

        outArr = []
        for elm in freqMap:
            if freqMap[elm] >= cutoffFreq:
                outArr.append(elm)

        return outArr


obj = Solution()
# print obj.topKFrequent([1,1,1,2,2,3], 2)
print obj.topKFrequent([3,0,1,0], 1)