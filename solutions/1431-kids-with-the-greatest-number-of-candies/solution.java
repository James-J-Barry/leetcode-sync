class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int kid : candies){
            if (max < kid){
                max = kid;
            }
        }
        ArrayList<Boolean> result = new ArrayList<Boolean>();
        int rec = max - extraCandies;
        for(int i = 0; i < candies.length; i++){
            result.add(candies[i] >= rec);
        }
        return result;
    }
}