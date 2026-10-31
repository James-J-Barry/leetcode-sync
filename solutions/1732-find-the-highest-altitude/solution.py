class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        max_altitude = 0
        for g in gain:
            if g < 0:
                if current_altitude > max_altitude:
                    max_altitude = current_altitude
            current_altitude += g
        return max(current_altitude,max_altitude)