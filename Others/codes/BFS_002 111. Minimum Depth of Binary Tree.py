# BFS
# LEARNING - BFS is better here because we are going level by level which is muchh better than DFS since we would find the solution earlier vs DFS where we will hhave tp traverse thhe complete tree to find thhe solution
# Major Learning: in BFS_001, we traversed BFS level by level. Over Here we traversed BFS node by node. Just something to keep in mind
# Also, note that I used queue in this example (very intuitive) [Node level: queue, depth level: simple for loop]
# Another thing is that I had to store depth along with the node (since this was node level and not depth level), so I used tuple of (node, depth) as the queue element



# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        queue = [(root, 1)]

        while queue:
            dequeued = queue.pop(0)
            if dequeued[0].left == None and dequeued[0].right == None:
                return dequeued[1]
            else:
                if dequeued[0].left != None:
                    queue.append((dequeued[0].left, dequeued[1]+1))
                if dequeued[0].right != None:
                    queue.append((dequeued[0].right, dequeued[1]+1))





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(2)

root.right.left = TreeNode(3)
root.right.right = TreeNode(2)

# root.left.left.right = TreeNode(3)
root.right.left.left = TreeNode(3)
root.right.right.right = TreeNode(2)


obj = Solution()
print obj.minDepth(root)
