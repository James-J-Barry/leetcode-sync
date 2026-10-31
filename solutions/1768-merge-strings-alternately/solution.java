class Solution {
    public String mergeAlternately(String word1, String word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        StringBuilder builder = new StringBuilder(l1 + l2);
        int a = Math.min(l1,l2);
        for (int i = 0; i < a; i++){
            builder.append(word1.charAt(i));
            builder.append(word2.charAt(i));
        }
        if(l1 < l2){
            while(a < l2){
                builder.append(word2.charAt(a));
                a++;
            }
        } else if (l1 > l2){
            while(a < l1){
                builder.append(word1.charAt(a));
                a++;
            }
        }
        return builder.toString();
    }
}