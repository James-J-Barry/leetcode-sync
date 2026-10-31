class Solution {
    public String longestCommonPrefix(String[] strs) {
        String pref = strs[0];
        for (String word : strs){
            for (int i = 0; i < pref.length(); i++){
                if (i >= word.length()){
                    pref = word;
                } else {
                    if (pref.charAt(i) != word.charAt(i)){
                        if (i == 0){
                            pref = "";
                        }
                        else {
                            pref = word.substring(0, i);
                        }
                    }
                }
            }
        }
        return pref;
    }
}