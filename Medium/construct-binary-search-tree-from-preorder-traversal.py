# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None

        def helper(root, num):
            if not root:
              return TreeNode(num)
            if root.val > num:
                root.left = helper(root.left, num)
            elif root.val < num:
                root.right = helper(root.right, num)
            
            return root
            
        for num in preorder:
          root = helper(root, num) 

        return root 