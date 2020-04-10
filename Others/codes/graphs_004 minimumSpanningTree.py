# spanning tree - all n nodes are connected, and there are n-1 edges, that is, there is no cycle in the graph
# minimum spanning tree - spanning tree with the minimum sum of edge weights
# Algorithms - Prim's and Kruskals (both work for negative egdes, but not for directed graphs) (both greedy)
# Prims - running time same as djikstras O(VlogV + E)

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
            return False

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

# graph structure
class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.edges = set()

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.nodeMap = {}
        self.visitedSet = set()

    def addNode(self, val):
        if val not in self.nodes:
            self.nodes.add(val)
            self.nodeMap[val] = GraphNode(val)
        return self.nodeMap[val]

    def addUndirectedEdge(self, vertex1, vertex2):
        node1 = self.addNode(vertex1)
        node2 = self.addNode(vertex2)

        node1.edges.add(node2)
        node2.edges.add(node1)

    def addDirectedEdge(self, vertex1, vertex2):
        node1 = self.addNode(vertex1)
        node2 = self.addNode(vertex2)

        node1.edges.add(node2)

    def dfsUndirectedStart(self):
        self.visitedSet = set()
        for node in self.nodeMap:
            if self.nodeMap[node] not in self.visitedSet:
                self.dfsUnDirected(self.nodeMap[node], None)

    def dfsUnDirected(self, vertex, incomingVertex):

        if vertex in self.visitedSet:
            print 'Cycle Exists'
            return
        self.visitedSet.add(vertex)
        print vertex.val

        for neighbor in vertex.edges:
            if neighbor != incomingVertex:
                self.dfsUnDirected(neighbor, vertex)

    def dfsDirectedStart(self):
        self.visitedSet = set()
        for node in self.nodeMap:
            if self.nodeMap[node] not in self.visitedSet:
                self.dfsDirected(self.nodeMap[node], set())

    def dfsDirected(self, vertex, parentSet):

        if vertex in parentSet:
            print 'Cycle Exists'
            return
        print vertex.val

        self.visitedSet.add(vertex)
        parentSet.add(vertex)

        for neighbor in vertex.edges:

            self.dfsDirected(neighbor, parentSet)
        # After complete visit, when I backtrack, then remove the element from the parent set
        parentSet.remove(vertex)

class WeightedUndirectedGraph(object):
    def __init__(self):
        self.nodes = set()
        self.nodeMap = {}
        # self.visitedSet = set()

    def addNode(self, val):
        if val not in self.nodes:
            self.nodes.add(val)
            self.nodeMap[val] = GraphNode(val)
        return self.nodeMap[val]

    def addWeightedUndirectedEdge(self, vertex1, vertex2, weight):
        node1 = self.addNode(vertex1)
        node2 = self.addNode(vertex2)

        node1.edges.add((node2, weight))
        node2.edges.add((node1, weight))

    def createWeightedUndirectedGraphFromEdgeList(self, edgeList, negateWeightsForMaxHeap=False):

        negate = 1
        if negateWeightsForMaxHeap:
            negate = -1

        for edge in edgeList:
            self.addWeightedUndirectedEdge(edge[0], edge[1], negate*edge[2])

    # Prim's Algorithm
    def minSpanningTreeWeightSum(self):

        # BoilerPlate
        # Create minHeap (maxHeap with negative weights to store min node weight. Initially, all nodes have infinite weight)
        priorityQueue = MaxHashHeap()
        # Populate the priorityQueue with inifinte weights
        for graphNode in self.nodes:
            priorityQueue.insertIntoHeap((-999999999, graphNode))

        # make one element priority as 0 which starts S
        priorityQueue.changeVal((0, priorityQueue.heapList[0][1]))

        minSpanningWightSum = 0
        S = set()
        # iterate all nodes
        for i in range(len(self.nodes)):

            # do extract min (max nagative)
            minNode = priorityQueue.popMax()
            if minNode[0] == -999999999:
                return -1
            minSpanningWightSum += minNode[0]
            S.add(minNode[1])

            minNodeGraph = self.nodeMap[minNode[1]]

            # look at all the edges connected to the extracted node and update the nighbor nodes with the weights
            # similar to 'relaxing' edges in dijkstra
            for connectedNode in minNodeGraph.edges:
                # consider nodes not already joined in S
                if connectedNode[0].val in S:
                    continue
                edgeWeight = connectedNode[1]
                connectedNodeGraphNodeVal = connectedNode[0].val
                # update the edge weight of the neighbor if the new weight is min than earlier node weight (bigger for negative weights)
                if edgeWeight > priorityQueue.heapList[priorityQueue.heapIndices[connectedNodeGraphNodeVal]][0]:
                    priorityQueue.changeVal((edgeWeight, connectedNodeGraphNodeVal))

        return -1*(minSpanningWightSum)



graph = WeightedUndirectedGraph()
# graph.createWeightedUndirectedGraphFromEdgeList([[1,2,5],[1,3,6],[2,3,1]], True)
# graph.createWeightedUndirectedGraphFromEdgeList([[1,2,5],[1,3,6],[2,3,1],[5,6,1]], True)
graph.createWeightedUndirectedGraphFromEdgeList([[1,2,3],[3,4,4]], True)
print graph.minSpanningTreeWeightSum()
# print graph



# Kruskal's algorithm

class DisjointSet(object):
    def __init__(self, value):
        self.rank = 0
        self.representedBy = value
        self.parent = None

class DisjoinSets(object):

    def __init__(self):
        # Hash table that stores the mappings of value -> node for fast access
        self.dictionarySets = {}

    # Create a set out of a new node
    def makeSet(self, value):
        node = DisjointSet(value)
        self.dictionarySets[value] = node

    # Find the value which represents the disjoint set containing val
    def findSet(self, val):

        # If the node has not be initialized till now, return False
        if val not in self.dictionarySets:
            return False

        startNode = self.dictionarySets[val]
        tempNode = startNode

        # Found the node. Now, travel up to find the parent
        while tempNode.parent != None:
            tempNode = tempNode.parent

        # Optimization
        # if tempNode is not the parent of startNode, then make it. This will make future findSet(startNode) faster
        if startNode != tempNode:
            startNode.parent = tempNode

        # tempNode here denotes the parent node
        return tempNode.representedBy


    # Join two sets together
    def union(self, a, b):

        aRepresentedBy = self.findSet(a)
        bRepresentedBy = self.findSet(b)

        # if either does not exist or both represented by same then simply return
        if (aRepresentedBy == False or bRepresentedBy == False) or (aRepresentedBy == bRepresentedBy):
            return

        # else, the parent is the one with the larger rank. Also, update the rank of the parent by incrementing it by 1
        if self.dictionarySets[aRepresentedBy].rank >= self.dictionarySets[bRepresentedBy].rank:
            self.dictionarySets[bRepresentedBy].parent = self.dictionarySets[aRepresentedBy]
            if self.dictionarySets[aRepresentedBy].rank == self.dictionarySets[bRepresentedBy].rank:
                self.dictionarySets[aRepresentedBy].rank += 1
        else:
            self.dictionarySets[aRepresentedBy].parent = self.dictionarySets[bRepresentedBy]
            if self.dictionarySets[bRepresentedBy].rank == self.dictionarySets[aRepresentedBy].rank:
                self.dictionarySets[bRepresentedBy].rank += 1

class Solution(object):
    def minimumCost(self, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Sort the edges by edge weight
        from operator import itemgetter
        connections = sorted(connections, key=itemgetter(2))

        makeSetDupCheck = set()
        disjointSet = DisjoinSets()
        minSpanningTreeWeightSum = 0
        setUnions = 0

        for edge in connections:
            vertex1 = edge[0]
            vertex2 = edge[1]
            weight = edge[2]

            # Do makeset on each graph vertex at least once
            if vertex1 not in makeSetDupCheck:
                makeSetDupCheck.add(vertex1)
                disjointSet.makeSet(vertex1)
            if vertex2 not in makeSetDupCheck:
                makeSetDupCheck.add(vertex2)
                disjointSet.makeSet(vertex2)

            # if the findSets are the same, we simply skip. if notm we do union of both
            if disjointSet.findSet(vertex1) != disjointSet.findSet(vertex2):
                disjointSet.union(vertex1, vertex2)
                minSpanningTreeWeightSum += weight
                setUnions += 1

        if setUnions == len(makeSetDupCheck)-1:
            return minSpanningTreeWeightSum
        else:
            return -1


obj = Solution()
print obj.minimumCost([[1,2,5],[1,3,6],[2,3,1]])
print obj.minimumCost([[1,2,5],[1,3,6],[2,3,1],[5,6,1]])
print obj.minimumCost([[1,2,3],[3,4,4]])

# graph.createWeightedUndirectedGraphFromEdgeList(, True)
# graph.createWeightedUndirectedGraphFromEdgeList(, True)
# graph.createWeightedUndirectedGraphFromEdgeList(, True)
