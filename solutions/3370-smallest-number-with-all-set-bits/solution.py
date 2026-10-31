class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        fin = 0
        while (fin < n):
            fin += 2**i
            i += 1
        return fin