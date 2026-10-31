class Solution {
    public boolean isArraySpecial(int[] nums) {
        if (nums.length <= 1){
            return true;
        } else {
            int last = nums[0] % 2;
            for(int i = 1; i < nums.length; i++){
                int num = nums[i] % 2;
                if (num == last){
                    return false;
                } else {
                    last = num;
                }
            }
        }
        return true;
    }
}