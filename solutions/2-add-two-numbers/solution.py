# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        lastdigit = dummy
        carryover = False
        current1 = l1
        current2 = l2
        while current1 or current2 or carryover:
            val1 = 0
            if current1:
                val1 = current1.val
                current1 = current1.next
            val2 = 0
            if current2:
                val2 = current2.val
                current2 = current2.next
            val3 = (1 if carryover else 0)
            total = val1 + val2 + val3
            if total >= 10:
                total %= 10
                carryover = True
            else:
                carryover = False
            lastdigit.next = ListNode(total, None)
            lastdigit = lastdigit.next
        return dummy.next