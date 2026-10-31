class Solution {
    public int removeElement(int[] nums, int val) {
        int[] copy = nums;
        int k = 0;
        int length = nums.length;
        for(int i = 0; i < length; i++){
            if(copy[i] != val){
                nums[k] = copy[i];
                k++;
            }
        }
        /*
        System.out.print("[");
        for(int l : nums){
            System.out.print(l + ", ");
        }
        */
        return k;
    }
}