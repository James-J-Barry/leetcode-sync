class Solution:
    def firstUniqChar(self, s: str) -> int:
        nonrepeatsord = []
        nonrepeats = set()
        repeats = set()
        for char in s:
            if not char in nonrepeats and not char in repeats:
                nonrepeats.add(char)
                nonrepeatsord.append(char)
            elif not char in repeats:
                nonrepeats.remove(char)
                nonrepeatsord.remove(char)
                repeats.add(char)
        return -1 if not nonrepeatsord else s.find(nonrepeatsord[0])