class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        m, n = len(grid), len(grid[0])
        numIslands = 0

        # O(R * C)
        for i in range(m):
            for j in range(n):
                if not (i,j) in visited and grid[i][j] == "1":
                    #found island -> do BFS to "visit" all cells in island
                    numIslands += 1
                    queue = deque([(i,j)])
                    visited.add((i,j)) #could be .append
                    while(queue):
                        r, c = queue.popleft() 
                        for rc, cc in DIRECTIONS:
                            nr, nc = r + rc, c + cc
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and not (nr,nc) in visited and grid[nr][nc] == "1":
                                queue.append((nr,nc))
                                visited.add((nr,nc))
        return numIslands



