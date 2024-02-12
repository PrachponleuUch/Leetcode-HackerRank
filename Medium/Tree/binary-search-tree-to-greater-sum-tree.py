# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def recursion(node, sum):
            if not node:
                return sum
            node.val += recursion(node.right, sum)
            return recursion(node.left, node.val)
        
        recursion(root, 0)
        return root

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        