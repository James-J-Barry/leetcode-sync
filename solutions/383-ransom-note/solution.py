class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magCounts = [0] * 26
        for char in magazine: 
            magCounts[ord(char) - 97] += 1
        ranCounts = [0] * 26
        for char in ransomNote:
            ranCounts[ord(char) - 97] += 1
        for i in range(0, 26):
            if ranCounts[i] > magCounts[i]:
                return False
        return True

        