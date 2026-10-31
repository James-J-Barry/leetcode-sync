class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ar = s.strip().split(" ")
        return len(ar[len(ar) - 1])