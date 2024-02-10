# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        q, qLength, current, ans = [root], 0, 0, 0
        while len(q):
            qLength, ans = len(q), 0
            for _ in range(qLength):
                current = q.pop(0)
                ans += current.val
                if current.left: q.append(current.left)
                if current.right: q.append(current.right)
        return ans
        """
        :type root: TreeNode
        :rtype: int
        """
        