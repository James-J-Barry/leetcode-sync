class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        nums = set(range(1,n+1))
        cols = defaultdict(set)
        rows = defaultdict(set)
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                rows[i].add(num)
                cols[j].add(num)
        for k in range(n):
            if rows[k] != nums or cols[k] != nums:
                return False
        return True