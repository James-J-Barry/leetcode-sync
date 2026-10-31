class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda iv: iv[0]) #sort by start time
        newIntervals = [intervals[0]]
        for i in range(1,len(intervals)):
            lastEnd = newIntervals[-1][1]
            start, end = intervals[i]
            if start <= lastEnd:
                newIntervals[-1] = [newIntervals[-1][0], max(lastEnd, end)]
            else:
                newIntervals.append(intervals[i])
        return newIntervals