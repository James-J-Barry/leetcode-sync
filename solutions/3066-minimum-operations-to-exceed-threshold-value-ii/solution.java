class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> ugh = new PriorityQueue<Long>();
        int times = 0;
        for(int num : nums){
            ugh.add(new Long(num));
        }
        while(!ugh.isEmpty()){
            Long u = ugh.poll();
            if (u >= k){
                break;
            }
            Long v = ugh.poll();
            times++;
            ugh.add(2*u + v);
        }
        return times;
    }
}