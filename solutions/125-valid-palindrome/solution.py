class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub(r'[\W_]', '', s).lower()
        return new == new[::-1]