class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int i = 0;
        int j = nums.length - 1;
        int total = 0;
        while (i < j){
            int a = k - nums[i];
            int b = nums[j];
            if(a == b){
                total++;
                i++;
                j--;
            } else if (a > b) {
                i++;
            } else {
                j--;
            }
        }
        return total;
    }
}