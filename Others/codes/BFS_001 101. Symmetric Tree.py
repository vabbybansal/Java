# BFS and Recursion

# LEARNING:
    # In recursion or any iterative approach, think of what are you operating on. For example, if the recursive function u make is for some operation on a node, do not mix and mingle thhat node's child in the operation'


# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# #
# # For example, this binary tree [1,2,2,3,4,4,3] is symmetric:


# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#
#         travStack = []
#
#         # Start traversal
#         if self.inOrder(root, travStack, root, 'push') == False or len(travStack) != 0:
#             return False
#         else:
#             return True
#
#         # # Once traversal is done, check for symmetricity
#         # # Check one: total elms - Odd
#         # totalNodes = len(travStack)
#         # if totalNodes%2 == 0:
#         #     return False
#         # # Check two: all elms in first half and second half should be sequentially the same
#         # for i in range((totalNodes-1)/2):
#         #     if travStack[i] != travStack[(totalNodes-1)/2 + 1 + i]:
#         #         return False
#
#         # if all checks get passed, code reaches here
#         # return True
#
#
#     def inOrder(self, node, travStack, root, mode):
#
#         # Base Case
#         if node == None:
#             return
#
#         # Go left subtree
#         self.inOrder(node.left, travStack, root, mode)
#
#         if node == root:
#             mode = 'pop'
#         elif mode == 'push':
#             travStack.append(node.val)
#         elif mode =='pop' and node!=root:
#             if travStack.pop() != node.val:
#                 return False
#
#
#         # # Access Element
#         # travList.append(node.val)
#
#         # Go right subtree
#         if self.inOrder(node.right, travStack, root, mode) == False:
#             return False


# # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True
        else:
            return self.nextFrontier([root.left, root.right])

    def nextFrontier(self, frontier):
        nextFront = []
        childVals = []

        currentFrontLen = len(frontier)
        CONTINUE = False

        # Traverse first half of the current frontier
        for i in range(currentFrontLen/2):

            # Add vals of current frontier to stack
            if frontier[i] != None:
                childVals.append(frontier[i].val)
                nextFront.append(frontier[i].left)
                nextFront.append(frontier[i].right)
                CONTINUE = True
            else:
                childVals.append(None)
                nextFront.append(None)
                nextFront.append(None)

        # Traverse and check the next half of the current frontier
        for i in range(currentFrontLen/2, currentFrontLen):

            leftPopped = childVals.pop()
            # Pop vals of current frontier to stack
            if frontier[i] != None:
                if frontier[i].val != leftPopped:
                    return False
                nextFront.append(frontier[i].left)
                nextFront.append(frontier[i].right)
            else:
                if None != leftPopped:
                    return False
                nextFront.append(None)
                nextFront.append(None)

        # If code reaches here, means the next frontier is safe. Send next frontier recursively
        # Check for base condition that is there is no next froniter (all Nones)
        if CONTINUE == True:
            return self.nextFrontier(nextFront)
        else:
            return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, root1 , root2):
        # If both trees are empty, then they are mirror images
        if root1 is None and root2 is None:
            return True

        """ For two trees to be mirror images, the following three 
            conditions must be true 
            1 - Their root node's key must be same 
            2 - left subtree of left tree and right subtree 
              of the right tree have to be mirror images 
            3 - right subtree of left tree and left subtree 
               of right tree have to be mirror images 
        """
        if (root1 is not None and root2 is not None):
            if  root1.val == root2.val:
                return (self.isMirror(root1.left, root2.right)and
                        self.isMirror(root1.right, root2.left))

                # If neither of the above conditions is true then root1
        # and root2 are not mirror images
        return False




# [1,2,2,3,4,4,3]
# [1,2,2,2,null,2]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(2)

obj = Solution()
print obj.isSymmetric(root)
