# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
# course 0. So the correct course order is [0,1] .
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
# courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

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
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Build graph
        graph = self.buildGraphFromEdgeList(prerequisites)

        # Add graph nodes without any edge
        for i in range(numCourses):
            if i not in graph.nodes:
                graph.nodes[i] = Node(i)

        # Detect directed cycle
        # If a directed cycle exists, then the course schedule is impossible. Return []
        if self.cycleDetect(graph): return []

        # Cycle does not exist and course schedule is possible
        return self.DAG_getOrder(graph)


    def DAG_getOrder(self, graph):

        stack = []
        visited = set()
        for node in graph.nodes:
            self.DAG_DFS(graph.nodes[node], stack, visited)

        return stack

    def DAG_DFS(self, node, stack, visited):

        if node.name in visited:
            return

        visited.add(node.name)

        for neighbor in node.edgeSet:
            self.DAG_DFS(neighbor, stack, visited)

        stack.append(node.name)


    def buildGraphFromEdgeList(self, edgeList):

        graph = Graph()

        for edge in edgeList:
            graph.addNode(edge[0])
            graph.addNode(edge[1])
            graph.addEdge(edge[0], edge[1])
        return graph

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


print Solution().findOrder(2, [[1,0]])
print Solution().findOrder(2, [])
print Solution().findOrder(2, [[1,0],[0,1]])
print Solution().findOrder(2, [[1,0]] )
print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])