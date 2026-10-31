# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)
        ino = inOrder(root)
        mindif = abs(ino[0] - ino[1])
        for i in range(1, len(ino) - 1):
            diff = abs(ino[i] - ino[i + 1])
            if diff < mindif:
                mindif = abs(ino[i] - ino[i + 1])
        return mindif