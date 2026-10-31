class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 1 && n == 1){
            return 1;
        }
        int[][] soln = new int[m][n];
        for(int i = 0; i < n - 1; i++){
            soln[m - 1][i] = 1;
        }
        for(int i = 0; i < m - 1; i++){
            soln[i][n - 1] = 1;
        }

        for(int i = m - 2; i >= 0; i--){
            for(int j = n - 2; j >=0; j--){
                soln[i][j] = soln[i + 1][j] + soln[i][j+1];
            }
        }
        return soln[0][0];
    }
}