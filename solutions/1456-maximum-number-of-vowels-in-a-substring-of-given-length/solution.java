class Solution {
    public int maxVowels(String s, int k) {
        Character[] vowarr = {'a', 'e', 'i', 'o', 'u'};
        HashSet<Character> vowels = new HashSet<Character>(Arrays.asList(vowarr));

        int maxVowels = 0;
        for (int i = 0; i < k; i++){
            if(vowels.contains(s.charAt(i))){
                maxVowels++;
            }
        }  

        int currentVowels = maxVowels;
        int len = s.length();
        for (int i = k; i < len; i++){
            if(vowels.contains(s.charAt(i))){
                currentVowels++;
            }
            if(vowels.contains(s.charAt(i - k))){
                currentVowels--;
            }
            if (currentVowels > maxVowels){
                maxVowels = currentVowels;
            }
        }
        return maxVowels;
    }
}