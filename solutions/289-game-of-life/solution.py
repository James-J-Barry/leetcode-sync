class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]
        m = len(board)
        n = len(board[0])
        for r in range(m):
            for c in range(n):
                count = 1
                for (rc, cc) in DIRECTIONS:
                    if (r + rc) < m and (r + rc) >= 0 and (c+cc) < n and (c+cc) >= 0:
                        #print(f"neighbor {(r + rc,c+cc)} of {(r,c)} is {board[r+rc][c+cc]}")
                        if board[r+rc][c+cc] > 0:
                            count +=1
                    #else:
                        #print(f"{(r,c)}: {(r+rc, c+cc)} not valid")
                if board[r][c] > 0:
                    board[r][c] = count
                else:
                    board[r][c] = -1 * count
        for r in range(m):
            for c in range(n):
                count = abs(board[r][c]) - 1
                if board[r][c] > 0:
                    if count == 2 or count == 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0
                else:
                    if count == 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0
        print(board)