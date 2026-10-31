class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        for (int i = 0; i < k; i++){
            // get min index
            int minI = 0;
            for (int m = 1; m < nums.length; m++){
                if (nums[m] < nums[minI]){
                    minI = m;
                }
            }
            nums[minI] = nums[minI] * multiplier;
        }
    return nums;
    }
}