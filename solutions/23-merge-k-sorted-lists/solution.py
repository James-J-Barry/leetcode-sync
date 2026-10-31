# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        result = []
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            nxt, lst = heapq.heappop(heap)
            result.append(nxt)
            if lists[lst]:
                heapq.heappush(heap, (lists[lst].val, lst))
                lists[lst] = lists[lst].next

        linkedResult = None if not result else ListNode(val=result[0])
        current = linkedResult
        for i in range(1,len(result)):
            current.next = ListNode(val=result[i])
            current = current.next
        return linkedResult
        