# Learning

# Cycle Detection in Directed Graph Problem

# Cycle Detection in Graphs
#   Undirected:
#       1) Union Find
#       2) DFS with a visited set. If a node traversed is already in the visited set, return True
#   Directed:
#       1) DFS with a visited and path set. Mark all the visited as visited and in path. Remove from path while backtracking, that is, at the end of the function. If we encounter a node which is already in path, return True. Note that, here, visited is only used on the outer level to prevent navigating the same visited node twice and keep the complexity linear in vertices and edges





# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.

class Graph(object):
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeName):
        if nodeName not in self.nodes:
            newNode = Node(nodeName)
            self.nodes[nodeName] = newNode

    def addEdge(self, nodeName1, nodeName2):
           self.nodes[nodeName1].edgeSet.add(self.nodes[nodeName2])

class Node(object):
    def __init__(self, nodeName):
        self.name = nodeName
        self.edgeSet = set()

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Build graph
        graph = self.buildGraphFromEdgeList(prerequisites)

        # Detect directed cycle
        return False if self.cycleDetect(graph) else True

    def cycleDetect(self, graph):

        visitedSet = set()
        for node in graph.nodes:
            if node in visitedSet:
                continue
            pathSet = set()
            if self.dfsDirectedCycleDetect(graph.nodes[node], visitedSet, pathSet):
                return True

    def dfsDirectedCycleDetect(self, node, visitedSet, pathSet):

        if node.name in pathSet:
            return True

        visitedSet.add(node.name)
        pathSet.add(node.name)

        for neighbor in node.edgeSet:
            if self.dfsDirectedCycleDetect(neighbor, visitedSet, pathSet):
                return True

        pathSet.remove(node.name)


    def buildGraphFromEdgeList(self, edgeList):

        graph = Graph()

        for edge in edgeList:
            graph.addNode(edge[0])
            graph.addNode(edge[1])
            graph.addEdge(edge[0], edge[1])
        return graph


print Solution().canFinish(2, [[1,0]])
print Solution().canFinish(2, [])
print Solution().canFinish(2, [[1,0],[0,1]])