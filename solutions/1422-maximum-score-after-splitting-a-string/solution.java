class Solution {
    public int maxScore(String s) {
        int max = 0;
        for (int i = 1; i < s.length(); i++){
            int score = 0;

            char[] left = new char[i];
            char[] right = new char[s.length() - i];
            
            s.getChars(0, i, left, 0);
            s.getChars(i, s.length(), right, 0);

            for (char c : left){
                if (c == '0'){
                    score++;
                }
            }
            for (char c : right){
                if (c == '1'){
                    score++;
                }
            }
            if (score > max){
                max = score;
            }
        }
        return max;
    }
}