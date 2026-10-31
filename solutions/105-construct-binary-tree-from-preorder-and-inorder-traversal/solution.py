# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        rootval = preorder[0]
        l = len(inorder)
        ind = inorder.index(rootval)
        leftInOrder = inorder[:ind]
        rightInOrder = [] if ind + 1 == l else inorder[ind + 1:]
        leftPreOrder = preorder[1:ind+1]
        rightPreOrder = preorder[ind+1:]
        root = TreeNode(val=rootval, left=self.buildTree(leftPreOrder,leftInOrder), right=self.buildTree(rightPreOrder,rightInOrder))
        return root