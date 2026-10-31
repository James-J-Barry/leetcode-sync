class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] num2Row = new int[m * n + 1];
        int[] num2Col = new int[m * n + 1];

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int num = mat[i][j];
                num2Row[num] = i;
                num2Col[num] = j;
            }
        }
        int[] rowTracker = new int[m];
        int[] colTracker = new int[n];
        for(int i = 0; i < arr.length; i++){
            int num = arr[i];
            rowTracker[num2Row[num]]++;
            colTracker[num2Col[num]]++;
            if(rowTracker[num2Row[num]] >= n ||
                colTracker[num2Col[num]] >= m){
                return i;
            }
        }
        return -1;
    }
}