class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int input = x;
        int rewindTime = 0;
        while (x > 0){
            rewindTime *= 10;
            rewindTime += (x % 10);
            x /= 10;
        }
        return (input == rewindTime);
    }
}