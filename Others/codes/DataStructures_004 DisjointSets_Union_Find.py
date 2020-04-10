
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


# Create disjointSet and do makesets
dSet1 = DisjoinSets()
dSet1.makeSet(1)
dSet1.makeSet(2)
dSet1.makeSet(3)
dSet1.makeSet(4)
dSet1.makeSet(5)
dSet1.makeSet(6)
dSet1.makeSet(7)

# Do union on sets
dSet1.union(1,2)
dSet1.union(3,2)
dSet1.union(4,5)
dSet1.union(6,7)
dSet1.union(5,6)
dSet1.union(3,7)

print 'yo'



