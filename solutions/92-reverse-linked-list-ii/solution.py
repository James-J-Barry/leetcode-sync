# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        prev = dummy
        current = head
        count = 1
        while count < left:
            prev = current
            current = current.next
            count += 1
        before = prev
        after = current
        while count <= right:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1
        before.next = prev
        
        after.next = current
        return dummy.next
        
        