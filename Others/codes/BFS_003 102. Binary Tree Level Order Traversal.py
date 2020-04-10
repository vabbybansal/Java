# BFS
# Did using level order traversal. Could have done it using queue with node level traversal as well, like BFS_0002


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        prevLevelNodes = [root]
        out = []

        while prevLevelNodes:

            levelNodes = []
            levelValList = []

            for node in prevLevelNodes:
                if node != None:
                    levelNodes.append(node.left)
                    levelNodes.append(node.right)
                    levelValList.append(node.val)

            if len(levelValList) != 0:
                out.append(levelValList)
            prevLevelNodes = levelNodes

        return out