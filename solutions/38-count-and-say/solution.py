class Solution:
    def countAndSay(self, n: int) -> str:
        def runLenEncode(str):
            result = ""
            current = str[0]
            count = 1
            for num in str[1:]:
                if num == current:
                    count += 1
                else:
                    result += f"{count}{current}"
                    current = num
                    count = 1
            result += f"{count}{current}"
            return result
        current = "1"
        for _ in range(n-1):
            current = runLenEncode(current)
        return current