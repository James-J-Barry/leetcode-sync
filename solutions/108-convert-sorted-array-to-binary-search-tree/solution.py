# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        median = floor(len(nums)/2)
        return TreeNode(val=nums[median], left=self.sortedArrayToBST(nums[:median]), right=self.sortedArrayToBST(nums[median + 1:]))