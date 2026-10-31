# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, p, q):
            if not root:
                return None
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            result = root if root == p or root == q else None
            if left and right:
                return root
            elif result:
                return root
            elif left:
                return left
            elif right:
                return right
            return None
        return helper(root, p, q)
