class Solution {
    public int tupleSameProduct(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length - 1; i++){
            for (int j = i + 1; j < nums.length; j++){
                int prod = nums[i] * nums[j];
                if (map.containsKey(prod)){
                    map.put(prod, map.get(prod) + 1);
                } else {
                    map.put(prod, 1);
                }
            }
        }
        int total = 0;
        for (Integer i : map.values()){
            if (i >= 2){
                total += i * (i - 1) * 4;
            }
        }
        return total;
    }
}