# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        toRemove = None
        remPrev = None
        current = head
        count = 0
        while current:
            count += 1
            if count == n:
                toRemove = head
            elif count == n + 1:
                toRemove = head.next
                remPrev = head
            elif count > n + 1:
                remPrev = toRemove
                toRemove = toRemove.next
            current = current.next
        if not toRemove and not remPrev:
            return head
        elif not remPrev:
            return head.next
        else:
            remPrev.next = toRemove.next
            return dummy.next


        