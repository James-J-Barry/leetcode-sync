# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -2000
        def recur(root):
            nonlocal best
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            if left + root.val + right > best:
                best = left + root.val + right
            return max(0, left + root.val, right + root.val)
        recur(root)
        return best


        
