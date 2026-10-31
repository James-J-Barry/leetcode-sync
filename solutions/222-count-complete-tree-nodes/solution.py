# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getLeft(root):
            current = root
            count = 0
            while current:
                count += 1
                current = current.left
            return count
        def getRight(root):
            current = root
            count = 0
            while current:
                count += 1
                current = current.right
            return count
        r = getRight(root)
        if r == getLeft(root):
            return sum([2**i for i in range(r)])
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1