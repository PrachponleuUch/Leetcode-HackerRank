# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if not nums: return null

    def helper(nums, start, end):
        if start > end: return 
        max_idx = start

        for i in range(start + 1, end + 1):
            if nums[i] > nums[max_idx]:
                max_idx = i
        
        root = TreeNode(nums[max_idx])

        root.left = helper(nums, start, max_idx-1)
        root.right= helper(nums, max_idx+1, end)

        return root

    return helper(nums, 0, len(nums) - 1)
    