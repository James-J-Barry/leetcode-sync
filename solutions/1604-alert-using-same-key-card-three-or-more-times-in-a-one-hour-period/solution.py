class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        timesByName = defaultdict(list)
        for i in range(len(keyName)):
            timesByName[keyName[i]].append(int("".join(keyTime[i].split(":"))))
        candidates = [name for name in timesByName.keys() if len(timesByName[name]) >= 3]
        culprits = []
        for candidate in candidates:
            times = sorted(timesByName[candidate])
            for i in range(2, len(times)):
                if times[i] <= times[i-2] + 100:
                    culprits.append(candidate)
                    break
        return sorted(culprits)