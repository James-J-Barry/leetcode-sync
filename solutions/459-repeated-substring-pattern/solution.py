class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        possible = range(1, floor(l/2) + 1)
        for i in possible:
            if l % i == 0:
                sub = s[:i]
                repeats = floor(l/i)
                if sub * repeats == s:
                    return True
        return False