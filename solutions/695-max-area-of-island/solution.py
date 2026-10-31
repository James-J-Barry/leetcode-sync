class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def bfsFindArea(grid, visited, sr, sc):
            m, n = len(grid), len(grid[0])
            DIRECTIONS = [(-1, 0),(1, 0),(0, -1),(0, 1)]
            totalArea = 0
            queue = deque()
            queue.append((sr,sc))
            while queue:
                r, c = queue.popleft()
                if not (r,c) in visited:
                    totalArea += 1
                    visited.add((r, c))
                    for rc, cc in DIRECTIONS:
                        nr, nc = r + rc, c + cc
                        if nr >= 0 and nr < m and nc >=0 and nc < n and not (nr, nc) in visited and grid[nr][nc] == 1:
                            queue.append((nr, nc))
            return totalArea

        m, n = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not (i, j) in visited:
                    area = bfsFindArea(grid, visited, i, j)
                    maxArea = max(maxArea, area)
        return maxArea