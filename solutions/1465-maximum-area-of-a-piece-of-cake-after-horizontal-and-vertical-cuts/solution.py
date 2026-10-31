class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        hlines = [0] + sorted(horizontalCuts) + [h]
        vlines = [0] + sorted(verticalCuts) + [w]

        def maxGap(lst):
            last = lst[0]
            gap = 0
            for i in range(len(lst)):
                if lst[i] - last > gap:
                    gap = lst[i] - last
                last = lst[i]
            return gap
        
        return (maxGap(hlines) * maxGap(vlines)) % ((10 ** 9) + 7)