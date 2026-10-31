class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current = list(s)
        if not current:
            return True
        i = 0
        for char in t:
            if char == current[i]:
                print(f"{current[i]}, {char}")
                i += 1
            if i == len(s):
                return True
        return False
