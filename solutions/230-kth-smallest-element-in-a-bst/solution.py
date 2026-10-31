# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)
        ino = inOrder(root)
        return ino[k - 1]