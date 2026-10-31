class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        HashMap<Integer, Integer> ballColor = new HashMap<Integer, Integer>();
        HashMap<Integer, HashSet<Integer>> ballsforeachcolor = new HashMap<Integer, HashSet<Integer>>();

        int[] result = new int[queries.length];
        for(int i = 0; i < queries.length; i++){
            int ball = queries[i][0];
            int color = queries[i][1];
            if (ballColor.containsKey(ball)){
                int ballscolor = ballColor.get(ball);
                ballsforeachcolor.get(ballscolor).remove(ball);
                if (ballsforeachcolor.get(ballscolor).isEmpty()){
                    ballsforeachcolor.remove(ballscolor);
                }
            }
            ballColor.put(ball, color);
            if (ballsforeachcolor.containsKey(color)){
                ballsforeachcolor.get(color).add(ball);
            } else {
                HashSet<Integer> add = new HashSet<Integer>();
                add.add(ball);
                ballsforeachcolor.put(color, add);
            }
            result[i] = ballsforeachcolor.size();
        }
        return result;
    }
}