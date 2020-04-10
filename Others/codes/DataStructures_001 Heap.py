class MaxHeap(object):

    # Invariant: Parent is always bigger than the children
    heapList = []

    def __init__(self):
        self.heapList = list()

    def insertIntoHeap(self, key):

        # Insert at the end of the heap array
        self.heapList.append(key)

        # Run maxHeapify on the last key
        self.maxHeapifyUp((len(self.heapList)-1))

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
    def maxHeapifyUp(self, nodeIndex):

        # if parent is smaller than the child, swap them
        while(self.hasParent(nodeIndex)) and self.parent(nodeIndex) < self.heapList[nodeIndex]:
            self.swap(self.getParentIndex(nodeIndex), nodeIndex)
            nodeIndex = self.getParentIndex(nodeIndex)

    # Correct the position of a single violation in the maxHeap by swapping parents and children
    def maxHeapifyDown(self, nodeIndex):

        # Check only if there is a child (left child first)
        while self.hasLeftChild(nodeIndex):
            biggerChildIndex = self.getLeftChildIndex(nodeIndex)

            # Check if we also have right child
            if self.hasRightChild(nodeIndex) and self.rightChild(nodeIndex) > self.leftChild(nodeIndex):
                biggerChildIndex = self.getRightChildIndex(nodeIndex)

            if self.heapList[nodeIndex] < self.heapList[biggerChildIndex]:
                self.swap(nodeIndex, biggerChildIndex)
                nodeIndex = biggerChildIndex
            else:
                return

    # Swap the parent and child nodes
    def swap(self, parentIndex, childIndex):

        tempVal = self.heapList[parentIndex]
        self.heapList[parentIndex] = self.heapList[childIndex]
        self.heapList[childIndex] = tempVal

    def popMax(self):

        if len(self.heapList) == 0:
            return False

        # If the max element has left child, start the process
        # Swap first element(max) with the last one, pop last, and run maxHeapify on the first element
        if self.hasLeftChild(0):
            self.swap(0, (len(self.heapList)-1))
            popped = self.heapList.pop()
            self.maxHeapifyDown(0)
        elif len(self.heapList) == 1:
            popped = self.heapList.pop()

        return popped

    def changeVal(self, nodeIndex, newVal):

        # If the new node value is less than the current node value, then replace and do maxHeapfy downwards
        if newVal < self.heapList[nodeIndex]:
            self.heapList[nodeIndex] = newVal
            self.maxHeapifyDown(nodeIndex)
        # If the new node value is more than the current node value, then replace and do maxHeapfy upwards
        elif newVal > self.heapList[nodeIndex]:
            self.heapList[nodeIndex] = newVal
            self.maxHeapifyUp(nodeIndex)
        else:
            return

    def deleteIndex(self, nodeIndex):

        # if it is the last element, simply pop
        if nodeIndex == len(self.heapList) - 1:
            self.heapList.pop()
            return

        # The item at index to be removed has to be exchanged with last the last item and the last item can then be popped out
        # Why this works? If we remove the last item from a max/min heap, it still retains its max / min property
        # Also, we can handle one violation using maxHeapify methods
        # This is the same as exchanging the node with the last, popping out last element and running maxHeapify

        # Remove last element
        lastElm = self.heapList.pop()

        # Run changeVal
        self.changeVal(nodeIndex, lastElm)

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

        if nodeIndex == len(self.heapList) - 1:
            self.heapList.pop()
            return

        # The item at index to be removed has to be exchanged with last the last item and the last item can then be popped out
        # Why this works? If we remove the last item from a max/min heap, it still retains its max / min property
        # Also, we can handle one violation using maxHeapify methods
        # This is the same as exchanging the node with the last, popping out last element and running maxHeapify

        # Remove last element
        lastElm = self.heapList.pop()

        # Run changeVal
        self.changeVal(nodeIndex, lastElm)


# myHeap = MaxHeap()
# myList = [10, 15, 20, 17, 1, 9, 2, 8, 3, 7, 10]

# # Insert into maxHeap
# for elm in myList:
#     myHeap.insertIntoHeap(elm)
#     print myHeap.heapList
#
# # Check heap sort
# # lenn = len(myHeap.heapList)
# # while lenn > 0:
# #     print myHeap.popMax()
# #     lenn = len(myHeap.heapList)
#
# # Change Value
# # myHeap.changeVal(8, 80)
# # print myHeap.heapList
#
# # Delete Value
# myHeap.deleteIndex(2)
# print myHeap.heapList
#
#
# lenn = len(myHeap.heapList)
# while lenn > 0:
#     print myHeap.popMax()
#     lenn = len(myHeap.heapList)

#
# myHeap = MinHeap()
# myList = [10, 15, 20, 17, 1, 9, 2, 8, 3, 7, 10]
#
# # Insert into minHeap
# for elm in myList:
#     myHeap.insertIntoHeap(elm)
#     print myHeap.heapList
# #
# # # Check heap sort
# lenn = len(myHeap.heapList)
# while lenn > 0:
#     print myHeap.popMin()
#     lenn = len(myHeap.heapList)
#
# # Change Value
# # myHeap.changeVal(8, 80)
# # print myHeap.heapList
#
# # Delete Value
# myHeap.deleteIndex(2)
# print myHeap.heapList
#
#
# lenn = len(myHeap.heapList)
# while lenn > 0:
#     print myHeap.popMax()
#     lenn = len(myHeap.heapList)