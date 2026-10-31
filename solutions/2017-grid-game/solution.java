class Solution {
    public long gridGame(int[][] grid) {
        
        long topRow = 0;
        long bottomRow = 0;
        int n = grid[0].length;

        for (int i = 1; i < n; i++){
            topRow += grid[0][i];
        }
        
        long min = topRow;
        for(int i = 1; i < n; i++){
            topRow -= grid[0][i];
            bottomRow += grid[1][i - 1];
            min = Math.min(Math.max(topRow, bottomRow), min);
        }

        return min;
        
        //previous solution that is wrong but i worked too long on to delete
        
        /*
        // sum all bottom row
        long max = grid[0][0];
        for (int i = 0; i < grid[0].length; i++){
            max += grid[1][i];
        }
        
        int goDown = 0;
        long current = max;
        for (int i = 1; i < grid[0].length; i++){
            current = current - grid[1][i-1] + grid[0][i];
            if (current > max){
                max = current;
                goDown = i;
            }
        }
        System.out.println(max);
        
        //blue robot either stays at the top the entire time or goes to the bottom immediately. 
        //since [0][0] is always 0, the number will either be the sum of the top row or the sum of the bottom row
        //account for where the 0s start(bottom row) or stop(top row)
        System.out.println(goDown);

        int sumtop = 0;
        for (int i = goDown + 1; i < grid[0].length; i++){
            sumtop += grid[0][i];
        }
        System.out.println(sumtop);

        int sumbottom = 0;
        for (int i = 0; i < goDown; i++){
            sumbottom += grid[1][i];
        }
        System.out.println(sumbottom);

        return (sumtop > sumbottom) ? sumtop : sumbottom;
        */
    }
}