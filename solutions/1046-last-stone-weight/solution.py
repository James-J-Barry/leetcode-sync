class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapMax = [-num for num in stones]
        heapq.heapify(heapMax)
        while len(heapMax) > 1:
            larger = -1 * heapq.heappop(heapMax)
            smaller = -1 * heapq.heappop(heapMax)
            if smaller < larger:
                heapq.heappush(heapMax, -1 * (larger - smaller))
        return 0 if not heapMax else -1 * heapMax[0]
        