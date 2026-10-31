class Solution {
    public int[] twoSum(int[] nums, int target) {
        int Nlength = nums.length;
        int[] solv = new int[2];
        boolean solved = false;
        for (int i = 0; i < Nlength; i++){
            for(int j = 0; j < Nlength; j++){
                if(((nums[i] + nums[j]) == target) && !solved && (i != j)){
                    solv[0] = i;
                    solv[1] = j;
                    solved = true;
                }
            }
        }
        return solv;
    }
}