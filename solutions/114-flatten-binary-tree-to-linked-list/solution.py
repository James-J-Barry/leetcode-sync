# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preOrder(node):
            if not node:
                return []
            return [node] + preOrder(node.left) + preOrder(node.right)
        pre = preOrder(root)
        pre = [] if not pre else pre[1:]
        current = root
        while pre:
            current.left = None
            current.right = pre[0]
            current = current.right
            pre = pre[1:]
        
