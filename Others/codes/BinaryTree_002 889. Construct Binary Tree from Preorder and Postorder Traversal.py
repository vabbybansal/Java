# Amazing logic to re-create the binary tree from preorder and postorder traversal information
# For such logic drivern questions, just try to form a pattern as to for example, where is the root. what is the left subtree
# and finally, validate that on an example of 2-3 test cases using dry run


# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
#
#
# Example 1:
#
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
#
# Note:
#
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        return self.createTree(pre, post)

    def createTree(self, pre, post):

        if len(pre) == 0 or len(post) == 0:
            return None

        root = pre[0]
        node = TreeNode(root)
        if len(pre) == 1:
            return node
        leftSubRoot = pre[1]

        for i in range(len(post)):
            if post[i] == leftSubRoot:
                break
        elmsLeftSub = i+1
        elmsRightSub = len(pre) - elmsLeftSub - 1

        node.left = self.createTree(pre[1:1+elmsLeftSub], post[0:elmsLeftSub])
        node.right = self.createTree(pre[1+elmsLeftSub:], post[elmsLeftSub:elmsLeftSub+elmsRightSub])

        return node

    def preOrder(self, node):

        if node == None:
            return

        print node.val
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):

        if node == None:
            return

        self.postOrder(node.left)
        self.postOrder(node.right)
        print node.val


obj = Solution()

obj.postOrder(obj.constructFromPrePost([2,1], [1,2]))
obj.preOrder(obj.constructFromPrePost([2,1], [1,2]))
# obj.preOrder(obj.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))
# print 'YEPEEEE'
# obj.postOrder(obj.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))

