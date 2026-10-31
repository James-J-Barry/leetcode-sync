class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rs = len(matrix)
        cs = len(matrix[0])
        rows, cols = set(), set()
        for r in range(rs):
            for c in range(cs):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in range(rs):
            for c in range(cs):
                if r in rows or c in cols:
                    matrix[r][c] = 0
        