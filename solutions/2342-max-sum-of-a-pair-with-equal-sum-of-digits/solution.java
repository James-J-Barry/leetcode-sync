class Solution {
    public int maximumSum(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int currentMax = -1;
        for(int i = 0; i < nums.length; i++){
            int sum = sumDigits(nums[i]);
            if(map.containsKey(sum)){
                int sol = nums[i] + map.get(sum);
                if (sol > currentMax){
                    currentMax = sol;
                }
                if (nums[i] > map.get(sum)){
                    map.put(sum, nums[i]);
                }
            } else {
                map.put(sum, nums[i]);
            }
        }
        return currentMax;
    }
    private int sumDigits(int num){
        int k = num;
        int sum = 0;
        while (k > 0){
            sum += k % 10;
            k/=10;
        }
        return sum;
    }
}