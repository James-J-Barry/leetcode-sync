class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        total = 0
        i = 0
        while i < l - 1:
            num = prices[i+1] - prices[i]
            if num > 0:
                total += num
            i += 1
        return total