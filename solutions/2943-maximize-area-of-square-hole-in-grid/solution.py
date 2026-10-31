class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def largestConsecutiveGap(lst):
            lst = sorted(lst)
            last = lst[0]
            inARow = 1
            maxRow = 1
            for i in range(1, len(lst)):
                if lst[i] == last + 1:
                    inARow += 1
                else:
                    inARow = 1
                if inARow > maxRow:
                    maxRow = inARow
                last = lst[i]
            return maxRow + 1

        hremovable = [num for num in hBars if num != 1 and num != n+2]
        vremovable = [num for num in vBars if num != 1 and num != m+2]
        return (min(largestConsecutiveGap(hremovable), largestConsecutiveGap(vremovable))) ** 2