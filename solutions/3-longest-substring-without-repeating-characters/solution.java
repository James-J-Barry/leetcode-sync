class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0){
            return 0;
        }
        int result = 1;
        HashSet<Character> set = new HashSet<>();
        set.add(s.charAt(0));
        int j = 0;
        int temp = 1;
        for (int i = 1; i < s.length(); i++){
            while (set.contains(s.charAt(i))){
                set.remove(s.charAt(j));
                j++;
                temp--;
            }
            set.add(s.charAt(i));
            temp++;
            if (temp > result){
                result = temp;
            }
        }
        return result;
    }
}