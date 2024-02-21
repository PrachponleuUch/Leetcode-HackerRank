# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0

        def helper(root, low, high):
            nonlocal answer
            if not root: return
            if low <= root.val <= high:
                answer += root.val
            helper(root.left, low, high)
            helper(root.right, low, high)
        
        helper(root, low, high) 
        return answer
        