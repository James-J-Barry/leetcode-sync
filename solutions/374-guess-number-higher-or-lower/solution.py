# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            num = (high + low) / 2
            result = guess(num)
            if result == 0:
                return num
            elif result > 0:
                low = num + 1
            else:
                high = num - 1