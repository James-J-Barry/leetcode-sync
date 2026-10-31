class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Convert each row to a tuple and count occurrences
        row_counts = Counter(tuple(row) for row in grid)
        count = 0

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += row_counts[col]
            
        return count
                    



                    
            