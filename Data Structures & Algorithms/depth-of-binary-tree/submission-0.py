# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length =0
        queue = deque()
        if root:    
            length = 1
            queue.append(root)
        
        while queue:
            curr = queue.popleft()
            if curr.left and curr.right:
                queue.append(curr.left)
                queue.append(curr.right)
                length+=1
            elif curr.left:
                queue.append(curr.left)
                length+=1
            elif curr.right:
                queue.append(curr.right)
                length+=1
        return length
        