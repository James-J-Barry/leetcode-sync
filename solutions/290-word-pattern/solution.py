class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        words = s.split(' ')
        wrdMap = {}
        seen = set()

        l = len(pattern)
        if l != len(words):
            return False
        for i in range(l):
            if pattern[i] in wrdMap:
                if wrdMap[pattern[i]] != words[i]:
                    return False
            elif words[i] in seen:
                return False
            else:
                wrdMap[pattern[i]] = words[i]
                seen.add(words[i])
        return True