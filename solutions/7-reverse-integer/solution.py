class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        final = 0
        k = abs(x)
        while (k > 0):
            final = (final * 10) + (k % 10) 
            k = int(k / 10) 
        if x < 0:
            final *= -1
        if (final > pow(2, 31) - 1) or (final < pow(2, 31) * -1):
            return 0
        return final
