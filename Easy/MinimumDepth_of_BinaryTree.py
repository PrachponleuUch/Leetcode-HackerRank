# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        def getMinDepth(root):
            if not root.left and not root.right:
                return 1
            elif root.left is None and root.right:
                return 1 + getMinDepth(root.right)
            elif root.right is  None and root.left:
                return 1 + getMinDepth(root.left)
            else:
                return 1 + min(getMinDepth(root.right),getMinDepth(root.left))
            
        return getMinDepth(root) if root else 0
        """
        :type root: TreeNode
        :rtype: int
        """
        