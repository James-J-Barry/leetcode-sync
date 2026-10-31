class Solution {
    private class Tuple {
        private int i;
        private int j;

        private Tuple(int first, int second){
            i = first;
            j = second;
        }
    }
    public int findMaxFish(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int max = 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                int fish = 0;

                boolean[][] visited = new boolean[m][n];

                Stack<Tuple> stack = new Stack<Tuple>();
                stack.push(new Tuple(i, j));

                while (!stack.isEmpty()){
                    Tuple current = stack.pop();
                    int x = current.i;
                    int y = current.j;

                    if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y] || grid[x][y] == 0) {
                        continue;
                    }

                    visited[x][y] = true;
                    fish += grid[x][y];

                    stack.push(new Tuple(x + 1, y));
                    stack.push(new Tuple(x - 1, y));
                    stack.push(new Tuple(x, y + 1));
                    stack.push(new Tuple(x, y - 1));
                }
                if (fish > max){
                    max = fish;
                }
            }
        }
        return max;
    }
    /*
    private int dfsFish(int i, int j, int m, int n, HashSet<Tuple> visited, int[][] grid){
        visited.add(new Tuple(i, j));
        if (i < 0 || i >= m || j < 0 || j >= n){
            return 0;
        }
        int toReturn = grid[i][j];
        if (!visited.contains(new Tuple(i-1, j))){
            toReturn += dfsFish(i-1, j, m, n, visited, grid);
        }
        if (!visited.contains(new Tuple(i+1, j))){
            toReturn += dfsFish(i+1, j, m, n, visited, grid);
        }
        if (!visited.contains(new Tuple(i, j-1))){
            toReturn += dfsFish(i, j-1, m, n, visited, grid);
        }
        if (!visited.contains(new Tuple(i-1, j+1))){
            toReturn += dfsFish(i, j+1, m, n, visited, grid);
        }
        return toReturn;
    }
    */
}