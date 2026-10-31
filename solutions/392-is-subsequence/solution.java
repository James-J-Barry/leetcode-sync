class Solution {
    public boolean isSubsequence(String s, String t) {
        int j = 0;
        boolean toReturn = false;
        int sl = s.length();
        int tl = t.length();
        if(sl == 0){
            return true;
        }
        for(int i = 0; i < tl; i++){
            if(s.charAt(j) == t.charAt(i)){
                j++;
            }
            if(j >= sl){
                toReturn = true;
                break;
            }
        }
        return toReturn;
    }
}