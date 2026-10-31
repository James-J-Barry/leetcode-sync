# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        result = False
        if not root.left and not root.right and root.val == targetSum:
            return True
        if root.left:
            result = result or self.hasPathSum(root.left, targetSum - root.val)
        if root.right and not result:
            result = result or self.hasPathSum(root.right, targetSum - root.val)
        return result
        
