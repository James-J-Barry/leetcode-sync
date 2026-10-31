class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        boolean leftGood = true;
        int totalSpaces = 0;
        for (int i = 0; i < flowerbed.length; i++){
            if (flowerbed[i] == 0){
                if((i == flowerbed.length - 1 || flowerbed[i + 1] == 0) && leftGood){
                    totalSpaces++;
                    leftGood = false;
                } else {
                    leftGood = true;
                }
            }else{
                leftGood = false;
            }
        }
        return (totalSpaces >= n);
        
        /*
        int totalSpaces = 0;
        int osinarow = 0;
        for (int pot : flowerbed){
            if (pot == 0){
                osinarow++;
            }else{
                totalSpaces += (osinarow - 1) / 2;
                osinarow = 0;
            }
        }
        return (totalSpaces >= n);
        */
    }
}