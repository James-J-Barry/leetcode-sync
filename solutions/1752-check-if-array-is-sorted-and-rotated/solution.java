class Solution {
    public boolean check(int[] nums) {
        boolean drop = false;
        HashSet<Integer> end = new HashSet<Integer>();
        int last = nums[0];
        int mingreatest = last;
        for (int num : nums){
            if (drop){
                if(num < last){
                    return false;
                }
                if (num > mingreatest){
                    return false;
                }
            }else{
                if(num < last){
                    drop = true;
                    if (num > mingreatest){
                        return false;
                    }
                }
            }
            last = num;
        }
        return true;
    }
}