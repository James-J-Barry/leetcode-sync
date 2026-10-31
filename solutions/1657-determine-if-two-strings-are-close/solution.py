class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1_chars = {}
        word2_chars = {}
        for char in word1:
            if char in word1_chars:
                word1_chars[char] += 1
            else:
                word1_chars[char] = 1
        for char in word2:
            if char in word2_chars:
                word2_chars[char] += 1
            else:
                word2_chars[char] = 1
        toReturn = True
        
        one_list = list(word1_chars.values())
        one_list.sort()
        two_list = list(word2_chars.values())
        two_list.sort()
        if not set(word1_chars.keys()) == set(word2_chars.keys()):
            toReturn = False
        elif not two_list == one_list:
            toReturn = False
        return toReturn
        