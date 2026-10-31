class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        wmax = 0
        while i < j:
            water = min(height[i], height[j]) * (j - i)
            if water > wmax: 
                wmax = water
            if height[i] < height[j]:
                i += 1
            else: 
                j -= 1
        return wmax