class Solution {
    public String removeOccurrences(String s, String part) {
        StringBuilder str = new StringBuilder(s);
        int len = part.length();
        for (int i = 0; i <= str.length() - len; i++){
            if (str.substring(i, i + len).equals(part)){
                str.delete(i, i + len);
                i = -1;
            }
        }
        return str.toString();
    }
}