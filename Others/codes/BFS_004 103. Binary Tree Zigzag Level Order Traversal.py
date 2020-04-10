# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#        3
#       / \
#      9  20
#        /  \
#       15   7
# return its zigzag level order traversal as:
# [
#     [3],
#     [20,9],
#     [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

tree = TreeNode()

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []
        elif root.val == None:
            return []


        toggle = False
        levelNodeList = [root]
        zigZagLevelOrder = []

        while True:
            toggle = not toggle
            posInsert = -1 if toggle else 0

            tempQ = []
            tempVals = []
            for i in range(len(levelNodeList)):
                if levelNodeList[i] == None:
                    continue
                if toggle:
                    tempQ.insert(0, levelNodeList[i].left)
                    tempQ.insert(0, levelNodeList[i].right)
                else:
                    tempQ.insert(0, levelNodeList[i].right)
                    tempQ.insert(0, levelNodeList[i].left)
                tempVals.append(levelNodeList[i].val)
            if len(tempVals) != 0:
                zigZagLevelOrder.append(tempVals)
                levelNodeList = tempQ
            else:
                break
        return zigZagLevelOrder