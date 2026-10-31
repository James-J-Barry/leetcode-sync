# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n = -1
        if not head.next:
            return None
        befRem = head
        current = head
        while current:
            n += 1
            if n % 2 == 1 and n > 2:
                befRem = befRem.next
            current = current.next
        toDel = befRem.next
        befRem.next = toDel.next
        return head
                