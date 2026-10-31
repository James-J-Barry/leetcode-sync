# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(self, maxInPath, root):
            if root == None:
                return 0
            val = root.val
            if val >= maxInPath:
                return 1 + helper(self, val, root.left) + helper(self, val, root.right)
            else:
                return helper(self, maxInPath, root.left) + helper(self, maxInPath, root.right)
        return helper(self, root.val, root)
