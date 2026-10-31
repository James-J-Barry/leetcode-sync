class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        toReturn = ""
        currentSum = sum
        currentNum = num
        while currentNum:
            digit = 9 if currentSum >= 9 else currentSum
            currentSum -= digit
            currentNum -= 1
            toReturn += str(digit)
        if currentSum:
            return ""
        return toReturn