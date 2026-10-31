class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda e: e[1])
        count = 1
        lastend = points[0][1]
        for balloon in points[1:]:
            if balloon[0] > lastend:
                count +=1
                lastend = balloon[1]
        return count