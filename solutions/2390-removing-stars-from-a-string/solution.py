class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for char in s:
            if (char == "*"):
                result = result[:-1]
            else:
                result += char
        return result