class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] reqChars = new int[26];

        // iterate through words2
        for (String word : words2){
            // count how many of each char there is in word
            int[] word2Chars = new int[26];
            for (char wrdChar : word.toCharArray()){
                word2Chars[((int) wrdChar) - 97] = word2Chars[((int) wrdChar) - 97] + 1;
            }
            // for each unique char in the word
            for (int i = 0; i < 26; i++){
                // if there are more of that char in the word than is currently 
                // in the reqChars, set the reqchars for that char
                if (word2Chars[i] > reqChars[i]){
                    reqChars[i] = word2Chars[i];
                }
            }
                
        }

        ArrayList<String> goodWords = new ArrayList<String>();

        // iterate through words1
    words:
        for (String word : words1){
            // count how many of each chars there is in word
            int[] word1Chars = new int[26];
            for (char wrdChar : word.toCharArray()){
                int charInd = ((int) wrdChar) - 97;
                word1Chars[charInd] = word1Chars[charInd] + 1;
            }
            // if each character has <= the amount in reqchar
            for (int i = 0; i < 26; i++){
                if (word1Chars[i] < reqChars[i]){
                    continue words;
                }
            }
            goodWords.add(word);
        }
        List<String> toReturn = goodWords;
        return toReturn;
    }
}