class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        has = set()
        for char in sentence:
            has.add(char)
        for char in "abcdefghijklmnopqrstuvwxyz":
            if not char in has:
                return False
        return True
