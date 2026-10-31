# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        rootval = postorder[-1]
        ind = inorder.index(rootval)
        l = len(inorder)
        leftIn = inorder[:ind]
        rightIn = [] if ind + 1 == l else inorder[ind + 1:]
        leftPost = postorder[:ind]
        rightPost = postorder[ind:-1]
        root = TreeNode(val=rootval, left=self.buildTree(leftIn, leftPost), right=self.buildTree(rightIn, rightPost))
        return root