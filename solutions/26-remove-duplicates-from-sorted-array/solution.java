class Solution {
    public int removeDuplicates(int[] nums) {
        /*
        int k = 0;
        int prevNum = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != prevNum){
                k++;
                prevNum = nums[i];
            }
            else if(i != nums.length - 1){
                nums[i] = nums[i+1];
                i--;
            }
        }
        return k;
        */
        int k = 1;
        int p = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != p){
                k++;
                p = nums[i];
            }
            nums[k - 1] = p;
        }
        return k;
    }
}