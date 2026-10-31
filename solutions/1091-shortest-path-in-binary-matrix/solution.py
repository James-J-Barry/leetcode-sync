class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        DIRECTIONS = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        length = 1

        if grid[0][0] == 1 or grid[m-1][n-1]:
            return -1

        queue = deque([(0,0)])
        visited = set([(0,0)])
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == m-1 and c == n-1:
                    return length
                for rc, cc in DIRECTIONS:
                    nr, nc = r+rc, c+cc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:
                        if not (nr,nc) in visited and grid[nr][nc] == 0:
                            queue.append((nr,nc))
                            visited.add((nr,nc))
            length += 1
        return -1