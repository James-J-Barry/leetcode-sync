class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ogColor = image[sr][sc]
        DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]
        m, n = len(image), len(image[0])

        #BFS
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for rc, cc in DIRECTIONS:
                nr, nc = r + rc, c + cc
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if not (nr,nc) in visited and image[nr][nc] == ogColor:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        return image
