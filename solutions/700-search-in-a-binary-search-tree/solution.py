# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return None
        v = root.val
        if val < v:
            return self.searchBST(root.left, val)
        elif val > v:
            return self.searchBST(root.right, val)
        else:
            return root
        