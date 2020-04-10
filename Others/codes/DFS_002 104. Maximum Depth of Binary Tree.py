# DFS
# Learning: DFS behavior can also be emulated by stack instead of using recursion. Solution below contains both ways

# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    MAX = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        # self.DFS(root, 1)
        self.DFS_STack(root)
        return self.MAX


    def DFS(self, node, level):

        # Base
        if node == None:
            if self.MAX < (level-1):
                self.MAX = level - 1
            return

        # Traverse
        self.DFS(node.left, level+1)
        self.DFS(node.right, level+1)

    def DFS_STack(self, root):

        stack = [(root, 1)]

        while stack:
            popped = stack.pop()
            if self.MAX < popped[1]:
                self.MAX = popped[1]

            if popped[0].left != None:
                stack.append((popped[0].left, popped[1]+1))
            if popped[0].right != None:
                stack.append((popped[0].right, popped[1]+1))




