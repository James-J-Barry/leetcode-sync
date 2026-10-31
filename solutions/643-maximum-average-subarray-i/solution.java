class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxVal = 0;
        for (int i = 0; i < k; i++){
            maxVal += nums[i];
        } 
        double curVal = maxVal;
        int len = nums.length;
        for (int i = k; i < len; i++){
            curVal += nums[i];
            curVal -= nums[i-k];
            if (curVal > maxVal){
                maxVal = curVal;
            }
        }
        return maxVal/k;
    }
}