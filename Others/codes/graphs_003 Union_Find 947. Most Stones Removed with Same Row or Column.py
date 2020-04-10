# 947. Most Stones Removed with Same Row or Column
# Medium
#
# 687
#
# 216
#
# Add to List
#
# Share
# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
#
# What is the largest possible number of moves we can make?
#
#
#
# Example 1:
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Example 2:
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Example 3:
#
# Input: stones = [[0,0]]
# Output: 0


class DisjointSet(object):
    # special case: value is a tuple (x,y) coordinates
    def __init__(self, value):
        self.rank = 0
        self.representedBy = (set([value[0]]), set([value[1]]))
        self.parent = None

class DisjoinSets(object):

    def __init__(self):
        # Hash table that stores the mappings of value -> node for fast access
        self.allConnectedComponents = set()

    # Create a set out of a new node
    def makeSet(self, value):
        node = DisjointSet(value)
        for component in list(self.allConnectedComponents):
            self.union(value, node, component)
        self.allConnectedComponents.add(node)

    # Join two sets together
    def union(self, tupleValue, node, component):
        if tupleValue[0] in component.representedBy[0] or tupleValue[1] in component.representedBy[1]:
            tupleX = node.representedBy[0].union(component.representedBy[0])
            tupleY = node.representedBy[1].union(component.representedBy[1])
            node.representedBy = (tupleX, tupleY)
            self.allConnectedComponents.remove(component)

class SolutionMine(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        connectedComponents = DisjoinSets()
        for stone in stones:
            connectedComponents.makeSet(stone)

        return len(stones) - len(connectedComponents.allConnectedComponents)

class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})


obj = Solution()
# print obj.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
# print obj.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])
# print obj.removeStones([[0,0]])
print obj.removeStones([[0,1],[1,0],[1,1]])


