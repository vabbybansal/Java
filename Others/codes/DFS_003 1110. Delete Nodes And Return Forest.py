# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#
#
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]


# Definition for a binary tree node.
class TreeNode(object):

    set_delete = set()
    outNodes = []

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """

        self.set_delete = set()
        self.outNodes = []

        self.set_delete = set(to_delete)

        if not self.DFS(root):
            self.outNodes.append(root)

        return self.outNodes


    def DFS(self, node):

        # Base case
        if node == None:
            return False

        leftReturn = self.DFS(node.left)
        if leftReturn:
            node.left = None
        rightReturn = self.DFS(node.right)
        if rightReturn:
            node.right = None

        if node.val in self.set_delete:
            self.set_delete.remove(node.val)
            if node.left is not None:
                self.outNodes.append(node.left)
            if node.right is not None:
                self.outNodes.append(node.right)
            return True


