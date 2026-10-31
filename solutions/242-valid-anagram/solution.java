class Solution {
    public boolean isAnagram(String s, String t) {
        int[] chrS = new int[26];
        for(char c : s.toCharArray()){
            chrS[((int) c) - 97] = chrS[((int) c) - 97] + 1;
        }
        int[] chrT = new int[26];
        for(char c : t.toCharArray()){
            chrT[((int) c) - 97] = chrT[((int) c) - 97] + 1;
        }
        for (int i = 0; i < 26; i++){
            if (chrS[i] != chrT[i]){
                return false;
            }
        }
        return true;
    }
}