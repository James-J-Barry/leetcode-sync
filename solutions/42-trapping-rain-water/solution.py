class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        amntWater = [0] * l
        for i in range(1,l - 1):
            totalhightleft = height[i - 1] + amntWater[i - 1]
            if totalhightleft > height[i]:
                amntWater[i] = totalhightleft - height[i]
        for i in range(l-2, -1, -1):
            currentHeight = height[i] + amntWater[i]
            totalhightright = height[i + 1] + amntWater[i + 1]
            if currentHeight > totalhightright:
                diff = currentHeight - totalhightright
                amntWater[i] = max(0, amntWater[i] - diff)
        return sum(amntWater)