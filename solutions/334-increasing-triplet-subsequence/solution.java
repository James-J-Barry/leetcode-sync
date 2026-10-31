class Solution {
    public boolean increasingTriplet(int[] nums) {
        int end = nums.length - 1;
        if (end < 2){
            return false;
        }
        int leftMin = nums[0];
        int[] maxRightofI = new int[end];
        maxRightofI[end - 1] = nums[end];
        for(int i = end - 2; i >= 0; i--){
            if (nums[i + 1] > maxRightofI[i + 1]){
                maxRightofI[i] = nums[i + 1];
            } else {
                maxRightofI[i] = maxRightofI[i + 1];
            }
        }
        for (int i = 1; i < end; i++){
            if (leftMin < nums[i] && nums[i] < maxRightofI[i]){
                return true;
            } else {
                if (nums[i] < leftMin){
                    leftMin = nums[i];
                }
            }
        }
    return false;
    }
}