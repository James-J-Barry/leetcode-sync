# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        lessdum = ListNode()
        nlessdum = ListNode()
        currentless = lessdum
        currentnless = nlessdum
        curr = head
        while curr:
            if curr.val < x:
                currentless.next = curr
                currentless = curr
                curr = curr.next

            else:
                currentnless.next = curr
                currentnless = curr
                curr = curr.next
        currentless.next = nlessdum.next
        currentnless.next = None
        current = lessdum.next
        return lessdum.next