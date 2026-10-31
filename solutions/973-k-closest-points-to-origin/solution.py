class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist(x, y):
            return sqrt(x**2 + y**2)
        keap = []
        for x, y in points:
            d = dist(x, y)
            pnt = (-d, (x, y))
            print(pnt)
            if not len(keap) == k:
                heapq.heappush(keap, pnt)
            else:
                if d < -1 * keap[0][0]:
                    heapq.heappop(keap)
                    heapq.heappush(keap, pnt)
        return [point for (d, point) in keap]
