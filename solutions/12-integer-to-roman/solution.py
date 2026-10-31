class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        current = num
        result = ""
        symbols = {"M": 1000, "CM":900, "D": 500, "CD":400, "C": 100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        sorted_keys = sorted(symbols, key=symbols.get)
        sorted_keys.reverse()
        for symbol in sorted_keys:
            value = symbols[symbol]
            while current >= value:
                current -= value
                result += symbol
        return result
        