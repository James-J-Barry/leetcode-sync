class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        #bfs
        m, n = len(grid), len(grid[0])
        queue = deque()
        DIRECTIONS = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        # every rotten orange is added to queue to start
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))

        count = 0
        while queue: 
            # repeat while there are unripe oranges
            for _ in range(len(queue)): 
                # all currently adjacent oranges
                r, c = queue.popleft()
                #check neighbors
                for rc, cc in DIRECTIONS:
                    nr, nc = r + rc, c + cc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
            if queue:
                count += 1
        #check for ripe orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return count
                    


        