class Solution {
    public int countServers(int[][] grid) {
        int[] rs = new int[grid.length];
        int[] cs = new int[grid[0].length];
        int total = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    rs[i]++;
                    cs[j]++;
                }
            }
        }
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1 && (rs[i] > 1 || cs[j] > 1)){
                    total++;
                }
            }
        }
        return total;
    }
}