# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        current1 = list1
        current2 = list2
        while current1 or current2:
            if current1 and not current2:
                curr.next = current1
                current1 = current1.next
                curr = curr.next
            elif current2 and not current1:
                curr.next = current2
                current2 = current2.next
                curr = curr.next
            else:
                if current1.val < current2.val:
                    curr.next = current1
                    current1 = current1.next
                    curr = curr.next
                else:
                    curr.next = current2
                    current2 = current2.next
                    curr = curr.next
        return dummy.next