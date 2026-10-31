class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ""
        l = len(s)
        maxRow = numRows - 1
        for i in range(min(numRows, l)):
            j = i
            result += s[j]
            inString = True
            while inString:
                #downphase
                move = maxRow - i
                if move != 0:
                    j += 2 * move
                    if j < l:
                        result += s[j]
                    else:
                        inString = False
                #upphase
                move = i
                if move != 0:
                    j += 2 * move
                    if j < l:
                        result += s[j]
                    else:
                        inString = False
        return result