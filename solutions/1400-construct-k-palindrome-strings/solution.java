class Solution {
    public boolean canConstruct(String s, int k) {
        // yuh
        if (k > s.length()){
            return false;
        
        // guh
        } else if (k == s.length()){
            return true;

        // real alorithm starts here:
        } else {

            // count frequency of each character in word
            int[] chars = new int[26];
            for (char c : s.toCharArray()){
                chars[((int) c) - 97] = chars[((int) c) - 97] + 1;
            }

            // count number of unique characters with odd counts 
            int odds = 0;
            for (int chr : chars){
                if (chr % 2 == 1){
                    odds++;
                } 
            }

            if (odds > k){
                return false;
            }
        }
        return true;
    }
}