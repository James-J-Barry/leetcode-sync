# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumHelper(root, total):
            if not root:
                return []
            total = (total * 10) + root.val
            if not root.left and not root.right:
                return [total]
            else:
                return [] + sumHelper(root.left, total) + sumHelper(root.right, total)
        sumList = sumHelper(root, 0)
        print(sumList)
        return sum(sumList)