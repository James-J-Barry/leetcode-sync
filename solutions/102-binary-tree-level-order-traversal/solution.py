# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque([root])
        result = []
        while queue:
            item = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    item.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if item:
                result.append(item)
        return result