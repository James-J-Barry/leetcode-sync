class Solution {
    public int longestOnes(int[] nums, int k) {
        int availableOnes = k;
        int currentLength = 0;
        int maxlength = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0){
                if (availableOnes > 0){
                    availableOnes--;
                    currentLength++;
                } else {
                    if (nums[i - currentLength] == 1){
                        currentLength--;
                        i--;
                    }
                }
            } else {
                currentLength++;
            }
            if (currentLength > maxlength){
                maxlength = currentLength;
            }
        }
        return maxlength;
    }
}