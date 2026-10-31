# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def recurFindPath(root):
            nonlocal best
            if not root:
                return 0
            left = recurFindPath(root.left)
            right = recurFindPath(root.right)
            if left + right > best:
                best = left + right
            return max(left, right) + 1
        recurFindPath(root)
        return best