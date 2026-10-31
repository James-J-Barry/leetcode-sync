class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        suffixMax = prices.copy()
        for i in range(len(prices)-2, -1, -1):
            suffixMax[i] = max(suffixMax[i], suffixMax[i+1])
        
        maxprof = max(0, suffixMax[1] - prices[0])
        minsofar = prices[0]
        for i in range(1,len(prices)-1):
            if prices[i] < minsofar:
                minsofar = prices[i]
                profit = max(0, suffixMax[i+1] - minsofar)
                if profit > maxprof:
                    maxprof = profit
        return maxprof