class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not (i,j) in visited:
                    #this means we have found an O cell in a region that we have not checked
                    region = set()
                    canEscape = False
                    #bfs it bruh
                    queue = [(i,j)]
                    while queue:
                        for _ in range(len(queue)):
                            a, b = queue.pop()
                            if a == 0 or b == 0 or a == m - 1 or b == n - 1:
                                canEscape = True
                            region.add((a,b))
                            visited.add((a,b))
                            for ac, bc in DIRECTIONS:
                                s, d = a+ac, b+bc
                                if s >=0 and s < m and d >= 0 and d < n and board[s][d] == "O" and (not (s,d) in visited):
                                    queue.append((s,d))
                    if not canEscape:
                        for a, b in region:
                            board[a][b] = "X"
                    
        



