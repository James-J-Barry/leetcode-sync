class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        known = {}
        def recursquares(known, n):
            if n in known:
                return known[n]
            if n < 4:
                return n

            largestsquarable = int(math.sqrt(n))
            minNum = n
            for i in range(largestsquarable, 0, -1):
                temp = recursquares(known, n - (i ** 2))
                if temp < minNum:
                    minNum = temp
            total = 1 + minNum
            known[n] = total
            return total
        return recursquares(known, n)

        
        