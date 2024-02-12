# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(node, gp, p):
            if not node:
                return
            if gp and gp.val % 2 == 0:
                self.ans += node.val
            helper(node.left, p, node)
            helper(node.right, p, node)
        helper(root, None, None)
        return self.ans

        