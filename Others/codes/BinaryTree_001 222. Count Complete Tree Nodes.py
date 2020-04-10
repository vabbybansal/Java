# Binary Tree
# LEARNINGS: if you are returning from a recursive method, then think about all the places where the code goes, as u ll have to fit in return something at each place, otherwise the function will return None
# Method:
# Get the height of the binary tree through DFS left traversal
# For missing items, start on the right till h-1, and check for the children to find the missing nodes
# Total nodes: Total possile nodes - missing

# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        def trav_height(node, level):

            # Base
            if node.left == None:
                return level

            h = trav_height(node.left, (level+1))

            return h

        # Get the height of the tree
        h = trav_height(root, 0)

        if h == 0:
            return 1

        def trav_right(node, level, count, found):
            # Base
            if level == h-1:
                if node.right == None:
                    count += 1
                else:
                    return count, 1
                if node.left == None:
                    count += 1
                else:
                    return count, 1

                return count, 0

            count, found = trav_right(node.right, level + 1, count, found)

            if found == 1:
                return count, found

            count, found = trav_right(node.left, level + 1, count, found)


            return count, found

        missing, found = trav_right(root, 0, 0, 0)

        return (2**(h+1)) -1 - missing




root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

obj = Solution()
print obj.countNodes(root)