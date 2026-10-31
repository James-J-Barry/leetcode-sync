class Solution {
    public String clearDigits(String s) {
        StringBuilder str = new StringBuilder(s);
        for (int i = 0; i < str.length(); i++){
            int c = (int) str.charAt(i);
            if(48 <= c && 57 >= c){
                str.deleteCharAt(i);
                i--;
                if(i >= 0){
                    str.deleteCharAt(i);
                    i--;
                }
            }
        }
        return str.toString();
    }
}