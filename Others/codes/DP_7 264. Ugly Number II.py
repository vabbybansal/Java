# Heap and DP
# Suboptimal solution - Heap
# I was able to make sense intuitively as to how the numbers would flow: subsequent multiplications by 2,3,5
# I got confused about how to handle till when to grow the tree, since the min might be one level down for some nodes of thhe 3 choices rather than same level
# Did not realize that, min would be still associated with all prev plus latest min pointers, and at eaah step, the min has to come from these
# Most optimum is the realization that all the future uglies are a multiple of previous uglies by 2,3 and 5.
#   So, lets say that the first uglies are 1,2,3,4... Future ones would be 2*1, 2*2, 2*3, 2*4, 2*5, 2*6, 2*8...., 3*1, 3*2, 3*3, 3*4, 3*5, 3*6, 3*8.... 5*1, 5*2, 5*3, 5*4, 5*5, 5*6, 5*8....
#   So, at anytime, the possible values to choose from for the next ugly would be min(2*[prevUglyOf2], 3*[prevUglyOf3], 5*[prevUglyOf5])
#   Hence, use memory of dynamic programming to utilize previously calculated uglies



# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.


# class Solution(object):
#
#     MEM = dict()
#
#     def checkMEM(self, num):
#         if num in self.MEM:
#             return self.MEM[num]
#
#     def isUgly(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num in self.MEM:
#             return self.MEM[num]
#
#         if num == 0:
#             return False
#
#         while num%2 == 0:
#             num = num/2
#             if self.checkMEM(num):
#                 return True
#
#         while num%3 == 0:
#             num = num/3
#             if self.checkMEM(num):
#                 return True
#
#         while num%5 == 0:
#             num = num/5
#             if self.checkMEM(num):
#                 return True
#
#         if num == 1:
#             return True
#         else:
#             return False
#
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         currentNum = 1
#         i = 0
#
#         while(i < n):
#
#             if self.isUgly(currentNum):
#                 self.MEM[currentNum] = True
#                 i += 1
#             else:
#                 self.MEM[currentNum] = False
#
#             currentNum += 1
#
#         return currentNum - 1
#
#
# obj = Solution()
# print obj.nthUglyNumber(10)


# class MinHeap(object):
#
#     # Invariant: Parent is always bigger than the children
#     heapList = []
#
#     def __init__(self):
#         self.heapList = list()
#
#     def insertIntoHeap(self, key):
#
#         # Insert at the end of the heap array
#         self.heapList.append(key)
#
#         # Run maxHeapify on the last key
#         self.minHeapifyUp((len(self.heapList)-1))
#
#     def hasParent(self, nodeIndex):
#         if nodeIndex > 0:
#             return True
#
#     def getParentIndex(self, nodeIndex):
#         return int((nodeIndex-1)/2)
#
#     def parent(self, nodeIndex):
#         return self.heapList[self.getParentIndex(nodeIndex)]
#
#     def getLeftChildIndex(self, nodeIndex):
#         return nodeIndex*2 + 1
#
#     def getRightChildIndex(self, nodeIndex):
#         return nodeIndex*2 + 2
#
#     def hasLeftChild(self, nodeIndex):
#         if self.getLeftChildIndex(nodeIndex) < len(self.heapList):
#             return True
#
#     def hasRightChild(self, nodeIndex):
#         if self.getRightChildIndex(nodeIndex) < len(self.heapList):
#             return True
#
#     def leftChild(self, nodeIndex):
#         return self.heapList[self.getLeftChildIndex(nodeIndex)]
#
#     def rightChild(self, nodeIndex):
#         return self.heapList[self.getRightChildIndex(nodeIndex)]
#
#     # Correct the position of a single violation in the maxHeap by swapping parents and children
#     def minHeapifyUp(self, nodeIndex):
#
#         # if parent is smaller than the child, swap them
#         while(self.hasParent(nodeIndex)) and self.parent(nodeIndex) > self.heapList[nodeIndex]:
#             self.swap(self.getParentIndex(nodeIndex), nodeIndex)
#             nodeIndex = self.getParentIndex(nodeIndex)
#
#     # Correct the position of a single violation in the maxHeap by swapping parents and children
#     def minHeapifyDown(self, nodeIndex):
#
#         # Check only if there is a child (left child first)
#         while self.hasLeftChild(nodeIndex):
#             smallerChildIndex = self.getLeftChildIndex(nodeIndex)
#
#             # Check if we also have right child
#             if self.hasRightChild(nodeIndex) and self.rightChild(nodeIndex) < self.leftChild(nodeIndex):
#                 smallerChildIndex = self.getRightChildIndex(nodeIndex)
#
#             if self.heapList[nodeIndex] > self.heapList[smallerChildIndex]:
#                 self.swap(nodeIndex, smallerChildIndex)
#                 nodeIndex = smallerChildIndex
#             else:
#                 return
#
#     # Swap the parent and child nodes
#     def swap(self, parentIndex, childIndex):
#
#         tempVal = self.heapList[parentIndex]
#         self.heapList[parentIndex] = self.heapList[childIndex]
#         self.heapList[childIndex] = tempVal
#
#     def popMin(self):
#
#         if len(self.heapList) == 0:
#             return False
#
#         # If the max element has left child, start the process
#         # Swap first element(max) with the last one, pop last, and run maxHeapify on the first element
#         if self.hasLeftChild(0):
#             self.swap(0, (len(self.heapList)-1))
#             popped = self.heapList.pop()
#             self.minHeapifyDown(0)
#         elif len(self.heapList) == 1:
#             popped = self.heapList.pop()
#
#         return popped
#
#     def changeVal(self, nodeIndex, newVal):
#
#         # If the new node value is less than the current node value, then replace and do minHeapfy downwards
#         if newVal > self.heapList[nodeIndex]:
#             self.heapList[nodeIndex] = newVal
#             self.minHeapifyDown(nodeIndex)
#         # If the new node value is more than the current node value, then replace and do minHeapfy upwards
#         elif newVal < self.heapList[nodeIndex]:
#             self.heapList[nodeIndex] = newVal
#             self.minHeapifyUp(nodeIndex)
#         else:
#             return
#
#     def deleteIndex(self, nodeIndex):
#
#         # The item at index to be removed has to be exchanged with last the last item and the last item can then be popped out
#         # Why this works? If we remove the last item from a max/min heap, it still retains its max / min property
#         # Also, we can handle one violation using maxHeapify methods
#         # This is the same as exchanging the node with the last, popping out last element and running maxHeapify
#
#         # Remove last element
#         lastElm = self.heapList.pop()
#
#         # Run changeVal
#         self.changeVal(nodeIndex, lastElm)
# class Solution(object):
#
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         if n == 1:
#             return 1
#
#         seenSet = set()
#         uglyMinHHeap = MinHeap()
#
#         lastUgly = 1
#         uglyMinHHeap.insertIntoHeap(lastUgly)
#
#         for i in range(n):
#             i2 = 2*lastUgly
#             i3 = 3*lastUgly
#             i5 = 5*lastUgly
#
#             if i2 not in seenSet:
#                 uglyMinHHeap.insertIntoHeap(i2)
#                 seenSet.add(i2)
#             if i3 not in seenSet:
#                 uglyMinHHeap.insertIntoHeap(i3)
#                 seenSet.add(i3)
#             if i5 not in seenSet:
#                 uglyMinHHeap.insertIntoHeap(i5)
#                 seenSet.add(i5)
#
#             lastUgly = uglyMinHHeap.popMin()
#
#         return lastUgly


class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglyArray = [0]*n
        uglyArray[0] = 1 # initializing with the first ugly number
        pointer2 = 0
        pointer3 = 0
        pointer5 = 0
        i = 0
        setUglies = set()

        for i in range(1, n):

            uglyArray[i] = min(2*uglyArray[pointer2], 3*uglyArray[pointer3], 5*uglyArray[pointer5])
            setUglies.add(uglyArray[i])

            if uglyArray[i] == 2*uglyArray[pointer2]:
                pointer2 += 1
            elif uglyArray[i] == 3*uglyArray[pointer3]:
                pointer3 += 1
            elif uglyArray[i] == 5*uglyArray[pointer5]:
                pointer5 += 1

            while 2*uglyArray[pointer2] in setUglies:
                pointer2 += 1
            while 3*uglyArray[pointer3] in setUglies:
                pointer3 += 1
            while 5*uglyArray[pointer5] in setUglies:
                pointer5 += 1

        return uglyArray[i]



obj = Solution()
print obj.nthUglyNumber(11)