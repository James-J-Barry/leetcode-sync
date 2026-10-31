class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
        result = mat.copy()

        visited = set()
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        rnd = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                result[i][j] = rnd
                #check neighbors
                for rc, cc in DIRECTIONS:
                    nr, nc = i + rc, j + cc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and not (nr,nc) in visited and mat[nr][nc] == 1:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            rnd += 1
        return result 
