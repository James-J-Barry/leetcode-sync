# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(val=6767, next=head)
        current = head
        prev = dummy
        lastUnique = dummy
        remvalue = 6767
        while current:
            if current.val == remvalue:
                lastUnique.next = current.next
                prev = lastUnique
            elif current.val == prev.val:
                remvalue = current.val
                prev = lastUnique
                prev.next = current.next
            else:
                lastUnique = prev
                prev = current
            current = current.next
        return dummy.next
        # current is none
        