"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def levelOrder(root):
            if not root:
                return
            queue = deque([root])
            while queue:
                l = len(queue)
                for i in range(l):
                    node = queue.popleft()
                    nextNode = None if i >= l - 1 else queue[0]
                    print(f"node {node.val} has next {"None" if not nextNode else nextNode.val}")
                    node.next = nextNode
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        levelOrder(root)
        return root