# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        curr = root
        def max_height(root):
            if root is None:
                return 0
            left_height = max_height(root.left)
            right_height = max_height(root.right)
            return max(left_height, right_height) + 1
        return max_height(root.left)+max_height(root.right)
