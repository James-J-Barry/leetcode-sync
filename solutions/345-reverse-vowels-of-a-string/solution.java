class Solution {
    public String reverseVowels(String s) {
        int i = 0;
        int j = s.length() - 1;
        HashSet<Character> vowels = 
            new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        StringBuilder result = new StringBuilder(s);

        while(i < j){
            char c1 = s.charAt(i);
            char c2 = s.charAt(j);

            if(vowels.contains(c1) && vowels.contains(c2)){
                result.setCharAt(i, c2);
                result.setCharAt(j, c1);
                i++;
                j--;
            } else if (vowels.contains(c1)){
                j--;
            } else if (vowels.contains(c2)){
                i++;
            } else {
                i++;
                j--;
            }
        }
        return result.toString();
        /*
        Stack<Character> stk = new Stack<Character>();
        HashSet<Character> vowels = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        for (int i = 0; i < s.length(); i++){
            if(vowels.contains(s.toLowerCase().charAt(i))){
                stk.push(s.charAt(i));
            }
        }
        StringBuilder result = new StringBuilder(s);
        for (int i = 0; i < s.length(); i++){
            if(vowels.contains(s.toLowerCase().charAt(i))){
                result.setCharAt(i, stk.pop());
            }
        }
        return result.toString();
        */
    }
}