class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        newboard = []
        for row in board:
            newrow = []
            for item in row:
                if item == ".":
                    newrow.append(0)
                else:
                    newrow.append(int(item))
            newboard.append(newrow)

        def isSectionSolvable(si, sj, ei, ej, b):
            numSet = set()
            for i in range(si, ei):
                for j in range(sj, ej):
                    if b[i][j] < 0 or b[i][j] > 9:
                        return False
                    if b[i][j] != 0:
                        if b[i][j] in numSet:
                            return False
                        else:
                            numSet.add(b[i][j])
            return True
        
        wholeBoardSolvable = True
        for i in range(0, 9):
            wholeBoardSolvable = wholeBoardSolvable and isSectionSolvable(i, 0, i+1, 9, newboard)
        for j in range(0, 9):
            wholeBoardSolvable = wholeBoardSolvable and isSectionSolvable(0, j, 9, j+1, newboard)
        for a in range(0, 3):
            for b in range(0, 3):
                wholeBoardSolvable = wholeBoardSolvable and isSectionSolvable(a * 3, b * 3, (a+1) * 3, (b + 1) * 3, newboard)
        return wholeBoardSolvable