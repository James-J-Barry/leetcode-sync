class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        leftRange = -1
        rightRange = len(costs)
        leftHeap = []
        rightHeap = []

        def addLeft(leftRange, rightRange, leftHeap, rightHeap):
            if leftRange + 1 < rightRange:
                leftRange = leftRange + 1
                heapq.heappush(leftHeap, costs[leftRange])
            return leftRange
        def addRight(leftRange, rightRange, leftHeap, rightHeap):
            if rightRange -1 > leftRange:
                rightRange = rightRange - 1
                heapq.heappush(rightHeap, costs[rightRange])
            return rightRange
        while leftRange < candidates - 1:
            leftRange = addLeft(leftRange, rightRange, leftHeap, rightHeap)
        while leftRange != rightRange - 1 and rightRange > len(costs) - candidates:
            rightRange = addRight(leftRange, rightRange, leftHeap, rightHeap)
        
        totalCost = 0
        for _ in range(k):
            if leftHeap and not rightHeap:
                totalCost += heapq.heappop(leftHeap)
                leftRange = addLeft(leftRange, rightRange, leftHeap, rightHeap)
            elif rightHeap and not leftHeap:
                totalCost += heapq.heappop(rightHeap)
                rightRange = addRight(leftRange, rightRange, leftHeap, rightHeap)
            elif leftHeap[0] > rightHeap[0]:
                totalCost += heapq.heappop(rightHeap)
                rightRange = addRight(leftRange, rightRange, leftHeap, rightHeap)
            else: 
                totalCost += heapq.heappop(leftHeap)
                leftRange = addLeft(leftRange, rightRange, leftHeap, rightHeap)
        return totalCost