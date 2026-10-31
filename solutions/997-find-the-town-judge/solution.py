class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        for a, b in trust:
            inDegree[b] += 1
            outDegree[a] += 1
        judges = [person for person in range(1,n+1) if inDegree[person] == n-1 and outDegree[person] == 0]
        return -1 if len(judges) != 1 else judges[0]
        