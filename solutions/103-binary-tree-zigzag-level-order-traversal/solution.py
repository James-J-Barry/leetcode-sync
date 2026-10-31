# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        for i in range(len(lst)):
            if i % 2 == 1:
                lst[i].reverse()
        return lst