class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {"M": 1000, "D": 500, "C": 100, "L":50, "X":10, "V":5, "I":1}
        total = 0
        l = len(s)
        i = 0
        while i < l:
            value = symbols[s[i]]
            if i < l - 1 and value < symbols[s[i + 1]]:
                total -= value
            else:
                total += value
            i +=1
        return total

        

        