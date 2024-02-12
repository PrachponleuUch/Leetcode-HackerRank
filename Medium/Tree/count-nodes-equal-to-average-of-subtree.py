# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        self.cnt = 0
        def traverse(node):
            if node is None:
                return (0, 0)
            total_left, count_left = traverse(node.left)
            total_right, count_right = traverse(node.right)

            count = count_left + count_right + 1
            total = total_left + total_right + node.val

            if node.val == total // count:
                self.cnt += 1
            
            return (total, count)
        traverse(root)
        return self.cnt

        """
        :type root: TreeNode
        :rtype: int
        """
        