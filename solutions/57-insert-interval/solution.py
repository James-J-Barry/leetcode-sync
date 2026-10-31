class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda e: e[0])
        result = [intervals[0]]
        for i in range(len(intervals)):
            last = result[-1]
            iv = intervals[i]
            if iv[0] <= last[1]:
                result[-1] = [last[0], max(iv[1], last[1])]
            else:
                result.append(iv)
        return result