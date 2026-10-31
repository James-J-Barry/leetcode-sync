class Solution {
    public int[] getNoZeroIntegers(int n) {
        for(int i = 1; i < n; i++){
            boolean works = true;
            int j = i;
            int k = n - i;
            while (j > 0){
                if (j % 10 == 0){
                    works = false;
                    break;
                }
                j /= 10;
            }
            if (works){
                while (k > 0){
                    if (k % 10 == 0){
                        works = false;
                        break;
                    }
                    k /= 10;
                }
            }
            if (works){
                int[] toreturn = new int[2];
                toreturn[0] = i;
                toreturn[1] = n-i;
                return toreturn;
            }
        }
        return null;
    }
}