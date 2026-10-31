# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfsValues(root):
            if not root:
                return []
            result, queue = [], deque([root])
            while queue:
                layer = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    layer.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(layer)
            return result
        lst = bfsValues(root)
        return [l[-1] for l in lst]

