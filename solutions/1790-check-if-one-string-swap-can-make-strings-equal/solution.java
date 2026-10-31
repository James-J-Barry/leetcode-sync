class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int[] oneDisc = new int[26];
        int[] twoDisc = new int[26];
        int len = s1.length();
        int disc = 0;
        for (int i = 0; i < len; i++){
            if (s1.charAt(i) != s2.charAt(i)){
                oneDisc[((int)s1.charAt(i)) - 97]++;
                twoDisc[((int)s2.charAt(i)) - 97]++;
                disc++;
                if (disc > 2){
                    return false;
                }
            }
        }
        if (Arrays.equals(oneDisc, twoDisc)){
            return true;
        }
        return false;
    }
}