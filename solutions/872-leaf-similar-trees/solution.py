# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def what(self, root):
            if root == None:
                return []
            left = what(self, root.left)
            right = what(self, root.right)
            if left == [] and right == []:
                return [root.val]
            else:
                lst = left + right
                return lst
        return (what(self, root1) == what(self, root2))
        