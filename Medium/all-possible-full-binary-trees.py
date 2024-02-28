# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = { 0: [], 1: [TreeNode()] }

        def helper(n):
            if n in memo:
                return memo[n]
            
            result = []
            for l in range(n):
                r = n - l - 1
                leftTree, rightTree = helper(l), helper(r)
                for lt in leftTree:
                    for rt in rightTree:
                        result.append(TreeNode(0, lt, rt))
            memo[n] = result
            return result
        return helper(n)
