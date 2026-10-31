"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hashm = {}
        current = head
        while current:
            newnode = Node(current.val)
            hashm[current] = newnode
            current = current.next
        current = head
        while current:
            curnewnode = hashm[current]
            curnewnode.next = None if not current.next else hashm[current.next]
            curnewnode.random = None if not current.random else hashm[current.random]
            current = current.next
        return None if not head else hashm[head]