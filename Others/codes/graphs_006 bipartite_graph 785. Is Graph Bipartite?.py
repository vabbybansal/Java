# Learning - Two methods
# Graph coloring and backtracking - good when we have edges instead of adjacency list
# Graph coloring and DFS - better when we have adjacency lists / the complete graph representation of each node
# For DFS, we would always need complete knowledge about the current node



# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
#
# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation:
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation:
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.

# Using graph coloration and backtracking
# https://www.youtube.com/watch?v=052VkKhIaQ4&t=790s
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        if len(graph) == 0 or len(graph) == 1:
            return True


        self.edges = []
        for i in range(len(graph)):
            for j in graph[i]:
                if j < i:
                    continue
                self.edges.append([i, j])

        self.dict1 = {}
        self.dict2 = {}
        return self.travPath(0, self.edges[0])

    def addVertexToDicts(self, vertex1, vertex2):
        if vertex1 in self.dict1:
            self.dict1[vertex1] += 1
        else: self.dict1[vertex1] = 1

        if vertex2 in self.dict2:
            self.dict2[vertex2] += 1
        else: self.dict2[vertex2] = 1

    def delVertexFromDicts(self, vertex1, vertex2):
        if self.dict1[vertex1] == 1:
            del self.dict1[vertex1]
        else: self.dict1[vertex1] -= 1

        if self.dict2[vertex2] == 1:
            del self.dict2[vertex2]
        else: self.dict2[vertex2] -= 1

    def travPath(self, edgeNum, edge):
        v1 = edge[0]
        v2 = edge[1]

        # validity of the edge
        if v1 in self.dict2 or v2 in self.dict1:
            return False

        # add vertex to dicts
        self.addVertexToDicts(v1, v2)

        # Base case
        if edgeNum >= len(self.edges)-1:
            return True

        # Navigate further in the paths
        newEdge = self.edges[edgeNum+1]
        # Travel one way
        if self.travPath(edgeNum+1, newEdge): return True
        # Travel other way
        if self.travPath(edgeNum+1, [newEdge[1], newEdge[0]]): return True

        # once travelled completely and still didn't find a true path, return false after unloading edge
        self.delVertexFromDicts(v1, v2)

        return False


# Using graph coloration and DFS
class Solution(object):
    def dfs(self, node, lastColor):
        if node not in self.colors:
            self.colors[node] = lastColor^1
        else:
            if self.colors[node] == lastColor:
                # Not Bipartite
                return True
            else: return False

        for neighb in self.graph[node]:
            if self.dfs(neighb, self.colors[node]): return True
    #
    def isBipartite(self, graph):
        self.graph = graph
        self.colors = {}
        for vertex in range(len(graph)):
            if vertex not in self.colors:
                if self.dfs(vertex, 0):
                    return False
        return True
    #     color = {}
    #     for node in xrange(len(graph)):
    #         if node not in color:
    #             stack = [node]
    #             color[node] = 0
    #             while stack:
    #                 node = stack.pop()
    #                 for nei in graph[node]:
    #                     if nei not in color:
    #                         stack.append(nei)
    #                         color[nei] = color[node] ^ 1
    #                     elif color[nei] == color[node]:
    #                         return False
    #     return True

obj = Solution()
print obj.isBipartite([[1,3], [0,2], [1,3], [0,2]])
print obj.isBipartite([[1],[0,3],[3],[1,2]])
print obj.isBipartite([[1,2],[0,2],[1]])
# print obj.isBipartite([[1],[0]])
# print obj.isBipartite([[1],[0,3],[1]])