class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def helper(board, word, coords, index, visited):
            # index is for the char we are looking for
            DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            if index == len(word):
                return True
            r, c = coords
            for rc, cc in DIRECTIONS:
                nr, nc = r + rc, c + cc
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and not (nr, nc) in visited:
                    if board[nr][nc] == word[index]:
                        visited.add((nr,nc))
                        if helper(board, word, (nr,nc), index + 1, visited):
                            return True
                        visited.remove((nr,nc))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if helper(board, word, (i,j), 1, set([(i,j)])):
                        return True
        return False

                    
            
