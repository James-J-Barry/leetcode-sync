class Solution {
    public int romanToInt(String s) {

        char[] charArray = s.toCharArray();

        HashMap<Character, Integer> symbols = new HashMap<Character, Integer>();
        symbols.put('I', 1);
        symbols.put('V', 5);
        symbols.put('X', 10);
        symbols.put('L', 50);
        symbols.put('C', 100);
        symbols.put('D', 500);
        symbols.put('M', 1000);

        int total = 0;

        int last = 0;
        for (int i = charArray.length - 1; i >= 0; i--){

            char tempChar = charArray[i];
            int temp = symbols.get(tempChar);
            if (temp < last){
                total -= temp;
            } else {
                total += temp;
            }
            last = temp;
        }

        return total;
    }    
}