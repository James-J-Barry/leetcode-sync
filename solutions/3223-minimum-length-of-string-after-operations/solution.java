class Solution {
    public int minimumLength(String s) {
        int length = s.length();

        int[] chars = new int[26];
        for (char wrdChar : s.toCharArray()){
            chars[((int) wrdChar) - 97] = chars[((int) wrdChar) - 97] + 1;
        }

        for (int freq : chars){
            int amount = freq;
            while (amount >= 3){
                amount -= 2;
                length -= 2;
            }
        }
        return length;
    }
}