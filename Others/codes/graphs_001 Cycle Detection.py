# Learnings:

# Cycle Detection in Graphs
#   Undirected:
#       1) Union Find
#       2) DFS with a visited set. If a node traversed is already in the visited set, return True
#   Directed:
#       1) DFS with a visited and path set. Mark all the visited as visited and in path. Remove from path while backtracking, that is, at the end of the function. If we encounter a node which is already in path, return True. Note that, here, visited is only used on the outer level to prevent navigating the same visited node twice and keep the complexity linear in vertices and edges

# Associated problems:
#   DFS_005 207. Course Schedule




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


# # Create disjointSet and do makesets
# dSet1 = DisjoinSets()
# dSet1.makeSet(1)
# dSet1.makeSet(2)
# dSet1.makeSet(3)
# dSet1.makeSet(4)
# dSet1.makeSet(5)
# dSet1.makeSet(6)
# dSet1.makeSet(7)
#
# # Do union on sets
# dSet1.union(1,2)
# dSet1.union(3,2)
# dSet1.union(4,5)
# dSet1.union(6,7)
# dSet1.union(5,6)
# dSet1.union(3,7)
#
# print 'yo'
#


# A - B - C
# |   |   |
# F   E - D
edges = [
    ['A', 'F'],
    ['A', 'B'],
    ['B', 'C'],
    ['B', 'E'],
    ['D', 'E'],
    ['D', 'C']
]

# Using Disjoint Sets
# -------------------
disjointSet = DisjoinSets()
# Do makeSet on each vertex.
# For each edge, do union of vertex.
#   If findSet is not same, means this edge will not create a cycle
#   If the findSet on the edge vertices is same at any point, it means cycle exists
vertexSeen = set()
for edge in edges:
    vertex1 = edge[0]
    vertex2 = edge[1]

    if vertex1 not in vertexSeen:
        vertexSeen.add(vertex1)
        disjointSet.makeSet(vertex1)

    if vertex2 not in vertexSeen:
        vertexSeen.add(vertex2)
        disjointSet.makeSet(vertex2)

    if disjointSet.findSet(vertex1) != disjointSet.findSet(vertex2):
        disjointSet.union(vertex1, vertex2)
    else:
        print 'Cycle Exists'


# Using DFS
# ---------
visitedSet = set()

# Create the graph
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


# graphObj = Graph()
# for edge in edges:
#     vertex1 = edge[0]
#     vertex2 = edge[1]
#     graphObj.addUndirectedEdge(vertex1, vertex2)
# print graphObj.nodes
# print graphObj.nodeMap
# graphObj.dfsStart()


directedEdges = [
    [1, 2],
    [2, 3],
    # [1, 4],
    # [4, 1],
    [1, 3],
    # [4, 5],
    # [5, 6],
    # [6, 4]
]
#  Normal DFS does not work for cycle detection in directed graph
# graphObj = Graph()
# for edge in directedEdges:
#     vertex1 = edge[0]
#     vertex2 = edge[1]
#     graphObj.addUndirectedEdge(vertex1, vertex2)
# print graphObj.nodes
# print graphObj.nodeMap
# graphObj.dfsStart()


# Modified DFS with parent awareness
# graphObj = Graph()
# for edge in directedEdges:
#     vertex1 = edge[0]
#     vertex2 = edge[1]
#     graphObj.addDirectedEdge(vertex1, vertex2)
# print graphObj.nodes
# print graphObj.nodeMap
# graphObj.dfsDirectedStart()

directedEdges = [
    [1, 2],
    [2, 3],
    [1, 3],
    [1, 4],
    # [4, 1],
    [4, 5],
    [5, 6],
    # [6, 4],
    [5, 3]
]
graphObj = Graph()
for edge in directedEdges:
    vertex1 = edge[0]
    vertex2 = edge[1]
    graphObj.addDirectedEdge(vertex1, vertex2)
print graphObj.nodes
print graphObj.nodeMap
graphObj.dfsDirectedStart()