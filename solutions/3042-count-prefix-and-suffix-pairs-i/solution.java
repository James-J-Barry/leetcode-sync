class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int count = 0;
        for (int i = 0; i < words.length - 1; i++){
            for(int j = i + 1; j < words.length; j++){
                if (isPrefixAndSuffix(words[i], words[j])){
                    count++;
                }
            }
        }
        return count;
    }
    private boolean isPrefixAndSuffix(String wrd, String bigWrd){
        boolean toReturn = false;
        int wrdLen = wrd.length();
        int bigWrdLen = bigWrd.length();
        if (wrdLen <= bigWrdLen){
            if(bigWrd.substring(0, wrdLen).equals(wrd) &&
                bigWrd.substring(bigWrdLen - wrdLen).equals(wrd)){
                    toReturn = true;
                }
        }
        return toReturn;
    }
}