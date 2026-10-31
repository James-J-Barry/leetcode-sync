class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        i, j = 0, 1
        l = len(s)
        length = 1
        chars = set([s[i]])
        while i < j and i < l and j < l:
            newChar = s[j]
            if newChar in chars:
                while True:
                    #remove characters from the start of substring until newChar
                    remChar = s[i]
                    i += 1
                    chars.remove(remChar)
                    length -= 1
                    if remChar == newChar:
                        break
            chars.add(newChar)
            length += 1
            j += 1
            if length > longest:
                longest = length
        return longest
        