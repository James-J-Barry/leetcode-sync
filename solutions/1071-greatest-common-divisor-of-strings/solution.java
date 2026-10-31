class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int maxLen = Math.min(str1.length(), str2.length());
        int max = 0;
        for (int i = 1; i <= maxLen; i++){
            if (str1.length() % i == 0 && str2.length() % i == 0){
                System.out.print(i);
                if (strDivides(str1.substring(0, i), str1) && strDivides(str1.substring(0, i), str2)){
                    System.out.print(" yay");
                    max = i;
                }
                System.out.println();
            }
        }
        return str1.substring(0, max);
    }
    private boolean strDivides(String subStr, String str){
        if (str.length() == 0){
            return true;
        } else if (str.substring(0, subStr.length()).equals(subStr)){
            return strDivides(subStr, str.substring(subStr.length()));
        }
        return false;
    }
}